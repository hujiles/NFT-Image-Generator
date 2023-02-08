# json
try:
    import json
except ImportError:
    package = 'json'
    os.system(f'pip install {package}')
    import json

# os
try:
    import os
except ImportError:
    package = 'os'
    os.system(f'pip install {package}')
    import os

# shutil
try:
    import shutil
except ImportError:
    package = 'shutil'
    os.system(f'pip install {package}')
    import shutil

# random
try:
    import random
except ImportError:
    package = 'random'
    os.system(f'pip install {package}')
    import random

# urllib.parse
try:
    import urllib.parse as up
except ImportError:
    package = 'urllib.parse'
    os.system(f'pip install {package}')
    import urllib.parse as up

# datetime
try:
    from datetime import datetime
except ImportError:
    package = 'datetime'
    os.system(f'pip install {package}')
    from datetime import datetime

# io
try:
    from io import BytesIO
except ImportError:
    package = 'io'
    os.system(f'pip install {package}')
    from io import BytesIO

# functs
try:
    import pyfuncts
except ImportError:
    package = 'pyfuncts'
    os.system(f'pip install {package}')
    import pyfuncts
 
# itertools
try:
    from itertools import product
except ImportError:
    package = 'itertools'
    os.system(f'pip install {package}')
    from itertools import product

# typing
try:
    from typing import Optional, Dict, List
except ImportError:
    package = 'typing'
    os.system(f'pip install {package}')
    from typing import Optional, Dict, List

# PIL
try:
    from PIL import Image
except ImportError:
    package = 'PIL'
    os.system(f'pip install {package}')
    from PIL import Image

# termcolor
try:
    from termcolor import cprint
except ImportError:
    package = 'termcolor'
    os.system(f'pip install {package}')
    from termcolor import cprint

# requests
try:
    from requests.sessions import Session
except ImportError:
    package = 'requests'
    os.system(f'pip install {package}')
    from requests.sessions import Session
    from requests.exceptions import HTTPError


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATETIME_FMT = '%Y-%m-%dT%H:%M:%S.%fZ'
UPLOAD_URL = 'https://api.pinata.cloud/pinning/pinFileToIPFS'
UPLOAD_JSON_URL = 'https://api.pinata.cloud/pinning/pinJSONToIPFS'
UA_HEADER = 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0'


class Config:
    # Constructor for the Config class
    def __init__(self, filename):
        # Store the filename passed as argument
        self.filename = filename
        # Initialize the data to None
        self.data = None

    # Implement the __getitem__ magic method
    def __getitem__(self, key):
        # If the data is not loaded yet, open the file and load the data
        if self.data is None:
            with open(self.filename) as conf:
                self.data = json.load(conf)
        # Return the value associated with the given key
        return self.data[key]

    # Implement the get method
    def get(self, key):
        # If the data is not loaded yet, open the file and load the data
        if self.data is None:
            with open(self.filename) as conf:
                self.data = json.load(conf)
        # Return the value associated with the given key using the get method
        return self.data.get(key)


class ImageSource:
    """Hold Image source data"""

    def __init__(self, directory: str, filename: str):
        self.directory = directory
        self.filename = filename
        self.rarity_rate = 1.0
        # Appearance counter
        self.counter = 0

    def __str__(self):
        return os.path.join(self.directory, self.filename)

    def __repr__(self):
        return self.__str__()

    def as_name(self):
        """File nome minus file extension"""
        return self.filename.split('.')[0]

    def full_path(self):
        """Full path of the image"""
        return os.path.join(BASE_DIR, self.directory, self.filename)


class ImageResult:
    """Hold Image result data"""
    # List of image source
    img_sources: List[ImageSource]

    def __init__(self, number: int,  img_sources: List[ImageSource]):
        self.number = number
        self.metadata = {}
        self.rarity = 0.0
        self.img_sources = img_sources
        self.buffer = None

    def __str__(self):
        return self.filename

    def __repr__(self):
        return self.__str__()

    @property
    def filename(self):
        return f'{self.number}.png'

    @property
    def upload_path(self):
        return f'images/{self.filename}.png'

    @property
    def json_upload_path(self):
        return f'json/{self.filename}.json'

    def full_path(self):
        """Full path of the image"""
        return os.path.join(BASE_DIR, 'output', 'images', self.filename)

    @property
    def json_full_path(self):
        """Full path of the image"""
        return os.path.join(
            BASE_DIR, 'output', 'metadata', f'{self.number}.json'
        )

    def save(self):
        """
        Save the image result
        and return Buffer to be sent to API
        """
        new_image = None
        attributes = []
        for img_src in self.img_sources:
            with Image.open(img_src.full_path()).convert('RGBA') as img:
                if new_image is None:
                    new_image = Image.new(mode='RGBA', size=img.size)
                new_image.paste(img, (0, 0), mask=img)

            trait_value = ' '.join(img_src.directory.split(' ')[:-1]).capitalize()
            attribute = {
                'trait_value': trait_value,
                'value': os.path.splitext(img_src.filename)[0]
            }
            attributes.append(attribute)

        # Save to file
        new_image.save(self.full_path())
        # Add metadata: attributes
        self.metadata.update({'attributes': attributes})

        # Buffer of current file that to be uploaded to API
        self.buffer = BytesIO()
        new_image.save(self.buffer, format='PNG')
        return attributes

    def save_metadata(self):
        with open(self.json_full_path, 'w') as fd:
            json.dump(self.metadata, fd, ensure_ascii=False, indent=4)


class Main:
    def __init__(self):
        self.http = Session()
        self.config = Config(os.path.join(BASE_DIR, 'config.json'))

        # List of image sources `ImageSource`
        self.img_sources = []
        # List of image result `ImageResult`
        self.img_results = []
        self.sum_of_rarity_rate = 0.0

        self.products = None
        # Dict of product and its rarity rate
        self.product_dict = {}

    def setup(self):
        # Result folders
        for folder in ['images', 'metadata']:
            os.makedirs(
                os.path.join(BASE_DIR, 'output', folder), exist_ok=True
            )

        # Count source file numbers
        possible_combinations = 1
        folder_files = []
        custom_rarity_rage = self.config.get('rarity')
        for folder in self.config['folders']:
            current_path = os.path.join(BASE_DIR, folder)
            os.makedirs(current_path, exist_ok=True)

            ignored = self.config['ignore'] or []

            num_files = 0
            file_list = []
            for filename in os.listdir(current_path):
                if filename in ignored:
                    # Skip ignored files
                    continue
                num_files += 1

                img_source = ImageSource(directory=folder, filename=filename)
                # Set image source rarity rate (default 1)
                cur_file_rarity = custom_rarity_rage.get(str(img_source))
                if cur_file_rarity == 0:
                    # current image rarity is 0, skipping
                    cprint(f'  Skipping 0% rarity image: {img_source}', 'red')
                    continue
                if cur_file_rarity is not None:
                    img_source.rarity_rate = float(cur_file_rarity)
                    self.sum_of_rarity_rate += float(cur_file_rarity)
                else:
                    img_source.rarity_rate = 1.0
                    self.sum_of_rarity_rate += 1.0

                self.img_sources.append(img_source)
                file_list.append(img_source)

            folder_files.append(file_list)
            possible_combinations *= num_files
            cprint(f'{current_path} contains {num_files} file(s)')

        if possible_combinations <= 0:
            cprint('Please make sure that all folders contain images', 'red')
            return False

        amount = self.config['amount']
        if amount > possible_combinations:
            shutil.rmtree('output')
            cprint(f"Can't make {amount} images, "
                   f"there are only {possible_combinations} possible combinations",
                   'red')
            return False

        # Image source file combinations
        self.products = list(product(*folder_files))
        self.prepare_randomization()

        cprint(f"Successfully created {amount} images", 'green')
        return True

    def prepare_randomization(self):
        """Preparation actions before `.set_list`"""
        counted_list = []
        cprint('\nImage rarity', 'magenta', attrs=['bold'])

        for p in self.products:
            rarity_rates = 0
            for item in p:
                rarity_rates += item.rarity_rate
                if item not in counted_list:
                    counted_list.append(item)
                    self.sum_of_rarity_rate += item.rarity_rate
            self.product_dict[p] = rarity_rates

        # Count mean of rarity rates
        sum_perc = 0.0
        for counted in counted_list:
            perc = round(counted.rarity_rate / self.sum_of_rarity_rate * 100, 2)
            cprint(f'  {counted.filename:20}: {perc:02} %')
            sum_perc += perc
        img_rarity_perc = round(sum_perc / len(counted_list), 2)
        cprint(f'Average : {img_rarity_perc} %\n', 'magenta', attrs=['bold'])

    def get_random(self):
        """Get random product"""
        sum_of_rarity = sum(self.product_dict.values())
        rand_score = random.randint(0, sum_of_rarity)
        score_count = 0
        choice = None
        for p, score in self.product_dict.items():
            score_count += score
            if rand_score <= score_count:
                choice = p
                break
        product_idx = self.products.index(choice)

        # Remove choice from `products` and `product_dict`
        self.products.pop(product_idx)
        del self.product_dict[choice]

        # Return product and its rarity rates
        rarity_rate = sum([c.rarity_rate for c in choice]) \
                      / self.sum_of_rarity_rate * 100
        return choice, round(rarity_rate, 2)

    def set_list(self):
        for num in range(self.config['amount']):
            choice, rarity_rate = self.get_random()
            img_result = ImageResult(num, choice)
            # save to file
            attributes = img_result.save()
            img_result.save_metadata()

            # Add metadata: description and name
            metadata = {
                'description': self.config['description'],
                'name': f'{self.config["project_name"]}#{img_result.number}',
                'rarity': rarity_rate,
                'attributes': attributes
            }
            img_result.metadata.update(metadata)
            self.img_results.append(img_result)

    def upload_all(self):
        cprint('\nUploading...\n', attrs=['bold'])

        image_files = []
        image_data = {}
        for img in self.img_results:
            image_files.append(('file', (
                f'images/{img.upload_path}', img.buffer.getvalue()
            )))
            img_name = f'{self.config["project_name"]}#{img.number}'
            image_data[img_name] = img.metadata

        metadata = {
            'name': self.config['project_name'],
            'description': self.config['description'],
            'keyvalues': image_data,
        }

        # images upload, retry 3 times
        count, response = 0, None
        while count <= 3:
            response = self.upload_files(image_files, metadata)
            count += 1
            if response is not None:
                break
        if count >= 3 or response is None:
            cprint('Images upload failed', 'red')
            return
        cprint(f'Images upload response: {json.dumps(response, indent=2)}',
               'green')

        ipfs_hash = response['IpfsHash']
        # the https version: f'https://gateway.pinata.cloud/ipfs/{ipfs_hash}'
        ipfs_url = f'ipfs://{ipfs_hash}'
        timestamp = datetime.strptime(response['Timestamp'], DATETIME_FMT)
        date = int(timestamp.timestamp() * 1000)

        json_files = []
        for img in self.img_results:
            img.metadata.update({
                'image': f'{ipfs_url}/' + up.quote(img.filename),
                'date': date
            })
            img.save_metadata()
            json_files.append(('file', (
                img.json_upload_path, open(img.json_full_path, 'rb')
            )))

        json_metadata = {
            'name': f'{self.config["project_name"]} metadata',
            'description': self.config['description'],
        }
        # images upload, retry 3 times
        count, response = 0, None
        while count <= 3:
            response = self.upload_files(json_files, json_metadata)
            if response is not None:
                break
            count += 1
        if count >= 3 or response is None:
            cprint('JSON upload failed', 'red')
            return
        cprint(f'JSON upload response: {json.dumps(response, indent=2)}',
               'green')

    def upload_files(self, files, metadata):
        try:
            resp = self.http.post(
                UPLOAD_URL,
                headers={
                    'Authorization': f'Bearer {self.config["api_key"]}',
                    'User-Agent': UA_HEADER
                },
                files=files,
                json={'pinataMetadata': json.dumps(metadata)},
                timeout=500,
            )
            resp.raise_for_status()
            response = resp.json()
            return response
        except HTTPError as exc:
            try:
                cprint(f'HTTP ERROR: {exc.response.json()}', 'red')
            except:
                cprint(f'HTTP ERROR: {exc}', 'red')
        except Exception as exc:
            cprint(f'ERROR: {exc}', 'red')

    def manual_upload_all(self):
        cprint('\nManual Upload...', 'green', attrs=['bold'])

        cprint('Metadata', 'green')
        ipfs_hash = input('IpfsHash: ')
        timestamp = input('Timestamp: ') or None

        # the https version: f'https://gateway.pinata.cloud/ipfs/{ipfs_hash}'
        ipfs_url = f'ipfs://{ipfs_hash}'
        if timestamp is not None:
            timestamp = datetime.strptime(timestamp, DATETIME_FMT)
            date = int(timestamp.timestamp() * 1000)
        else:
            date = None

        for img in self.img_results:
            img.metadata['image'] = f'{ipfs_url}/' + up.quote(img.filename)
            if date is not None:
                img.metadata['date'] = date
            img.save_metadata()

        cprint(f'JSON metadata is updated...', 'green')

    def save_gif(self):
        assert self.img_results, 'Result images is not saved'

        frames = []
        # for img in self.img_results:
        for img in self.img_results[:self.config['profile_images']]:
            frames.append(Image.open(img.full_path()))

        frames[0].save(
            os.path.join(BASE_DIR, 'output', 'profile.gif'),
            format='GIF',
            append_images=frames[1:],
            save_all=True, duration=230, loop=0
        )


def main():
    m = Main()
    m.setup()
    m.set_list()

    ## API upload
    m.upload_all()

    ## For manual files upload
    #m.manual_upload_all()

    m.save_gif()


if __name__ == '__main__':
    main()
