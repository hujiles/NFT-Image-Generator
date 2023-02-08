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

def startprint():
    """Specifies printing"""
    sys.stdout = sys.__stdout__

def get_a_proxy():
    """When using spammy commands that could get ratelimited a proxy should be used"""
    """Proxy format : http://user:pass@ip:port OR http://ip:port depending on your proxies"""
    """No proxies? If you want some look into buying residential user & pass ones, or use the program without (return None)"""
    return f"http://user:pass@ip:port" #http://ip:port also works

def clear():
    """Clears screen"""
    try:
        os.system("cls")
    except:
        pass

def pprint(text,color,spacing=0):
    """This lets me print stuff nicely and if I choose to change the interface I won't need to edit lots of individual print statements"""
    spacestr = spacing * " "
    print(f"{color}[{spacestr}{Fore.WHITE}{text}{color}{spacestr}]{Fore.WHITE}")


def ai_headers(authorisation_token):
    """Gives our requests HEADERS as the name suggests - this makes the site think we're on a certain device, got referred from a certain place, and are allowed to do what we're doing (sites don't like programs spamming)!"""
    return {
'accept':'*/*',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-GB,en;q=0.8',
'authorization':f'bearer {authorisation_token}',
'content-type':'text/plain;charset=UTF-8',
'origin':'https://www.wombo.art',
'referer':'https://www.wombo.art/',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'cross-site',
'sec-gpc':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
'x-app-version':'WEB-1.90.1',
}

def make_title(content):
    os.system(f"title {content}")

def get_style():
    """Will add all soon - found an efficient way. These style ids are what the website uses and the words in front are what you can input - it's easier to know your intentions by typing cartoon as oppose to 57"""
    term_to_style = {
    "trippy":57,
    "cartoon":58,
    "realistic":32,
    "vibrant":6,
    "painted":50,
    "none":3,
    "street_art":41,
    "high_quality":7,
    "meme":44,
    }
    for thing in term_to_style:
        pprint(f"{thing.upper()}",Fore.CYAN)
    while True:
        try:
            pprint("Please input a style (one of the above)",Fore.GREEN)
            inp = input().lower().replace("[","").replace("]","")
            styleid = term_to_style[inp]
            return styleid
        except:
            pprint(f"Invalid term",Fore.RED)


def download_image(url,filepath):
    """Downloads an image off the cdn"""
    while True:
        try:
            data = httpx.get(url)
            break
        except:
            pass
    f = open(filepath,"wb")
    f.write(data.content)
    f.close()

def get_combos(mainthing):
    """Some styles - when you get every single possibility you end up with LOTS of varieties!"""
    colors = [["COLOR"],["red","orange","green","light blue","dark blue","purple","black","white","silver"]];colors = [colors[0],[f"{x} {mainthing}" for x in colors[1]]];colors = [f"{colors[0][0]}|{x}" for x in colors[1]]
    materials = [["MATERIAL"],["gold","diamond","platinum"]];materials = [materials[0],[f"made of {x}" for x in materials[1]]]
    foods = [["FOOD"],["burger","pizza","chicken","chips","ice cream","hotdog","drink"]];foods = [foods[0],[f"eating {x}" for x in foods[1]]]
    headwear = [["HEADWEAR"],["halo","hat","baseball cap","christmas hat","antenna","mask","gasmask","goggles","eyepatch","beanie","blindfold"]];headwear = [headwear[0],[f"with {x}" for x in headwear[1]]]
    backwear = [["BACKWEAR"],["wings","backpack","shopping bag"]];backwear = [backwear[0],[f"wearing {x}" for x in backwear[1]]]
    wearables = [["WEARABLE"],["chain","necklace","ring"]];wearables = [wearables[0],[f"wearing {x}" for x in wearables[1]]]
    personalities = [["PERSONALITY"],["happy","sad","bored","excited","crazy","hypnotised","mad"]];personalities = [personalities[0],[f"that is {x}" for x in personalities[1]]]

    choices = [colors]
    for possibility in [materials,foods,headwear,backwear,wearables,personalities]:
        while True:
            pprint(f"Do you want these {possibility[0][0]} features : {possibility[1]}",Fore.CYAN)
            pprint(f"1/Y = YES",Fore.GREEN)
            pprint(f"2/N = NO",Fore.GREEN)
            inp = input().upper()
            if inp in ["1","Y","YES"]:
                new_list = [f"{possibility[0][0]}|{x}" for x in possibility[1]]
                #print(new_list)
                choices.append(new_list)
                pprint("ADDED",Fore.GREEN)
                break
                
            elif inp in ["2","N","NO","0"]:
                pprint("DISCARDED",Fore.RED)
                break 
            else:
                pprint("Invalid input",Fore.RED)
    pprint("Getting combinations",Fore.GREEN)
    all_combos = list(itertools.product(*choices))
    random.shuffle(all_combos)
    pprint(f"Made {len(all_combos)} combinations!",Fore.GREEN)
    pprint(f"Type ALL to keep all or input a number of these that you would like to keep!",Fore.GREEN)
    try:
        keep = int(input())
    except:
        keep = "ALL"
    if keep != "ALL":
        if keep > len(all_combos):
            pprint(f"{keep} is more then you have ({len(all_combos)})...",Fore.RED)
        elif keep == len(all_combos):
            pprint(f"{keep} is equal to what you have ({len(all_combos)})...",Fore.RED)
        else:
            all_combos = all_combos[0:keep]
    pprint(f"you now have {len(all_combos)} combinations",Fore.GREEN)
    return all_combos

            
def format_features(list):
    """Formats it so that we don't have attribute names in our prompt"""
    stringlist = ""
    for thing in list:
        stringlist += f'{thing.split("|")[1]} '
    return stringlist.strip()

def format_features_for_attributes(metadata,list):
    """Used for getting json attribute data formatted correctly"""
    
    for thing in list:
        listdict = {}
        listdict["trait_type"] = thing.split("|")[0]
        listdict["value"] = str(thing.split("|")[1]).lower().replace("made of ","").replace("eating ","").replace("with ","").replace("wearing ","").replace("that is ","")
        metadata["attributes"].append(listdict)
    return metadata


def write_json_data(file_path,content,iindent=4):
    """Writes json data to a specific file path"""
    with open(file_path,"w") as f:
        json.dump(content,f,indent=iindent)



def ai_task(attributes,description,styleid,mainidea,count,tries=10,delay=6):
    """Uses wombo.ai's api with the authorisation token we made"""
    try:
        prompt = format_features(attributes)
        authorisation_token = get_ai_auth_token()
        if authorisation_token == None:
            return 
        session = httpx.Client(headers=ai_headers(authorisation_token),timeout=30)
        r = session.post(f"https://paint.api.wombo.ai/api/tasks",json={"premium":False})
        #print(r.text)
        if 'id' not in r.json():
            pprint(f"Task creation error : {r.text}",Fore.RED)
        task_id = r.json()["id"]


        r = session.put(f"https://paint.api.wombo.ai/api/tasks/{task_id}",json={"input_spec":{"prompt":f"{prompt}","style":styleid,"display_freq":10}})
        #print(r.text)

        for i in range(tries):
            try:
                r = session.get(f"https://paint.api.wombo.ai/api/tasks/{task_id}")
                time.sleep(delay)
                if r.json()["state"] == "completed":
                    pprint(f"Finished making : [{prompt}]",Fore.GREEN)
                    break
            except:
                pass
    
        cdn = r.json()["result"]["final"]
        if cdn != None:

            metadata = {
                'name': f'{mainidea} #{count}',
                'description': f"{description}",
                'image': f'{cdn}',
                'attributes': []
            }
            metadata = format_features_for_attributes(metadata,attributes)
            download_image(cdn,f"{mainidea}./{count}.png")
            write_json_data(f"{mainidea}./{count}.json",metadata)

            return True
        else:
            pprint(f"Error making : {prompt}",Fore.RED)
    except Exception as e:
        print(e)
        return False



def get_ai_auth_token(key="AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw"):
    """This is used to get an authorisation header for wombo - making it seem like we're a user. They key used for googleapis is the same everytime!"""
    try:
        token = httpx.post(f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={key}",proxies=get_a_proxy(),headers={'accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9','content-type':'application/json','origin':'https://www.wombo.art','sec-ch-ua':'"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'cross-site','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-client-version':'Chrome/JsCore/9.1.2/FirebaseCore-web',}
,json={"returnSecureToken":True}).json()["idToken"]
        pprint(f"Generated authorisation token for api requests : {token[:60]}.......",Fore.GREEN)
    except Exception as e:
        return None
        #pprint("Error getting header for wombo.art - please open https://www.wombo.art/create with a network debugger and search for 'bearer' inside the requests",Fore.RED)
        #pprint("Please input it below...",Fore.CYAN)
        #token = input("")
    return token



def ai_creation():
    """Using wombo.art and reversing it so that we can mass create images"""
    pprint("Using an AI service to CREATE images",Fore.GREEN,1)
    colors = ["red","orange","green","light blue","dark blue","purple","black","white","silver"]
    #authorisation_token = get_ai_auth_token()
    pprint(f"What general theme (ape/penguin whatever you want etc)",Fore.GREEN)
    mainidea = input("")
    try:os.mkdir(f"{mainidea}")
    except:pass
    features = get_combos(mainidea)
    styleid = get_style()
    pprint(f"NFT Description?",Fore.GREEN)
    description = input()
    #print(f"Style ID : {styleid}")
    pprint(f"Thread count (do 75 if you're not sure!)",Fore.GREEN)
    progress_counter = 0
    try:
        thread_count = int(input())
    except:
        thread_count = 75
    
    for featurecombo in features:
        progress_counter += 1
        while threading.active_count() >= thread_count:
            time.sleep(0.1)
        threading.Thread(target = ai_task, args = (featurecombo,description,styleid,mainidea,progress_counter)).start()
        make_title(f"{progress_counter}/{int(len(features))}")    



def opensea_scraper(crypto="ETHEREUM",file_type="PNG"):
    """You need to input a collection address NOT a name"""
    pprint("Please input a collection ADDRESS!",Fore.CYAN,1)
    inp = input().lower()
    pprint("Thread count - Put a number around 50 if you're not sure!",Fore.GREEN)
    try:threadcount = int(input())
    except:threadcount = 50
    image_count = 0
    try:os.mkdir(f"{inp}")
    except:pass
    url = f"https://api.rarible.org/v0.1/items/byCollection?collection={crypto}:{inp}"
    continuation = None
    while True:
        if continuation != None:
            new_url = url + f"&continuation={continuation}"
        else:new_url = url
        #pprint(f"{new_url}",Fore.GREEN)
        r = httpx.get(new_url)
        try:
            for object in r.json()["items"]:
                image_count += 1
                token_id = object["tokenId"]
                image_url = object["meta"]["content"][0]["url"]
                #pprint(f"{token_id} - {image_url}",Fore.GREEN)
                while threading.active_count() > threadcount:
                    time.sleep(0.1)
                try:
                    filename = int(token_id)
                except:
                    filename = f"{image_count}"
                threading.Thread(target = download_image, args = (image_url,f"./{inp}./{filename}.{file_type}")).start()
                pprint(f"{image_count} - Downloading token : {token_id}",Fore.GREEN)
                make_title(f"Progress : {image_count}")
        except:
            pass
        if 'continuation' not in r.json():
            pprint(f"All {image_count} items scraped!",Fore.GREEN)
            break 
        else:
            continuation = r.json()["continuation"]


def get_file_extension(ffile):
    """Reverses the file name in case there are multiple .s to get the guarenteed filename then flips it back around"""
    try:
        reversedfile = ffile[::-1]
        fileextensionreversed = reversedfile.split(".")[0]
        fileextensionnotreversed = fileextensionreversed[::-1]
        return f".{fileextensionnotreversed}"
    except:
        return ""

def name_sorter():
    """Sorts a folders photos from random to 1,2,3,4,5, etc"""
    pprint("Please input a folder name",Fore.GREEN)
    foldername = input()
    all_files = os.listdir(f"./{foldername}")
    pprint("Please input a base name to rename to (can be empty) (will result in basename 1 , basename 2 etc)",Fore.GREEN)
    basename = input()
    if len(basename) != 0:
        basename += " " #so there's a space if there is an input
    counter = 1;renamed=0;errorrenaming=0
    for thing in all_files:
        try:
            current_path = os.path.join(foldername,thing)
            new_file_name = f"{basename}{counter}{get_file_extension(thing)}"
            desired_path = os.path.join(foldername,new_file_name)
            os.rename(current_path,desired_path) 
            pprint(f"Renamed {thing} to {new_file_name}",Fore.GREEN)
            counter += 1;renamed += 1
        except Exception as e:
            pprint(f"Error renaming {thing} | {e}",Fore.RED)
            errorrenaming += 1 
        make_title(f"Renamed {counter} Error renaming {errorrenaming}")
    pprint(f"Finished renaming {renamed} files",Fore.GREEN)



def main():
    """Organiser of program"""
    clear()
    startprint()
    pprint("Please input an option!",Fore.GREEN,1)
    pprint(f"1 OR AI for AI created nfts",Fore.GREEN)
    pprint(f"2 OR SCRAPE to scrape a collection",Fore.GREEN)
    pprint(f"3 OR NAME to name order a bunch of files",Fore.GREEN)
    inp = input().upper()
    if inp in ["1","AI"]:
        ai_creation()
    elif inp in ["2","SCRAPE"]:
        opensea_scraper()
    elif inp in ["3","NAME"]:
        name_sorter()
    else:
        pprint(f"Invalid input?",Fore.RED)

main()
pprint(f"Finished",Fore.RED)
input()
