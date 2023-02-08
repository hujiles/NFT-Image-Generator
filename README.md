# NFT-Image-Generator
Fork by [huji](https://github.com/hujiles), rewritten and advanced
Utility for creating a generative art collection from supplied image layers, especially made for making NFT collectibles.

<details>
  <summary>Click here for example images.</summary>
  
  <img width="168" alt="final_images" src="https://user-images.githubusercontent.com/78478073/148702504-228edc50-692f-4f2c-ae0a-d815593edbd4.JPG"> <img width="168" alt="eyes" src="https://user-images.githubusercontent.com/78478073/148820162-1ac65e98-a9a2-43b5-9b7e-5569f1e00c08.JPG"> <img width="168" alt="clothes_hats" src="https://user-images.githubusercontent.com/78478073/148820218-d247a9dc-e020-4f7f-a839-751ec15898bd.JPG"> <img width="168" alt="body_horns" src="https://user-images.githubusercontent.com/78478073/148820292-9a3c306f-e0a7-4fd7-a2b4-7ae988636099.JPG"> <img width="168" alt="backgrounds" src="https://user-images.githubusercontent.com/78478073/148820011-c82acf21-87ae-460f-8a50-bb15e82d0083.JPG">
  
</details>

## Prerequisites
1. Clone the repository by opening your Terminal and typing ```git clone https://github.com/sem/NFT-Image-Generator.git```.
2. Install the dependencies ```pip3 install -r requirements.txt```.

## How to use
1. Get an API key from [Pinata](https://app.pinata.cloud/keys).
2. Open ``config.json`` and put the JWT (Secret access token) in ``api_key``.
3. Adapt the config to your liking and make sure there is a sequential number at the beginning of each folder to represent the order of layers.
4. Run ``main.py``.

## File structure
Before you start, make sure your file structure looks something like this:
```
NFT-Image-Generator/
├─ main.py
├─ config.json
├─ 1 background/
│  ├─ red.png
│  ├─ green.png
│  ├─ blue.png
├─ 2 body/
│  ├─ female.png
│  ├─ male.png
│  ├─ zombie.png
├─ 3 eyes/
│  ├─ sun_glasses.png
│  ├─ normal_eyes.png
│  ├─ vr_glasses.png
```

## Features
- [x] Generate metadata for direct use on [OpenSea](https://docs.opensea.io/docs/metadata-standards).
  - [x] Being able to update the image URL after the metadata is created.
- [x] Automatically upload images and metadata to [Pinata](https://www.pinata.cloud).
- [x] Ensure that no duplicate images will appear in the collection.
- [x] Create a .GIF profile picture for your collection.
- [x] Give each image a rarity value. 
  - [x] Influence rarity by giving layers a weight.
