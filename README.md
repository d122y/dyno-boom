# NFT image generator

A simple image generator that iterates through base image collections in the in/ folder and for each base image replaces colors according to defined palettes, followed by recursively applying optional accessories. The result is dumped to the out/ folder.

For example, given the base image ![Base image](./in/d-rex/d-rex/png)

Accessories ![hands](./in/d-rex/hands/mug.png) ![head](./in/d-rex/head/beanie.png)

And defined palettes (./Palettes.py)
```
	Palette("pink-on-yellow", (241,249,2), (201,0,181), (71,2,64))	
```

It'll generate
![colors replaced](./out/d-rex/d-rex_pink-on-yellow.png) ![beanie](./out/d-rex/d-rex_pink-on-yellow_beanie.png) ![mug](./out/d-rex/d-rex_pink-on-yellow_mug.png) ![mug and beanie](./out/d-rex/d-rex_pink-on-yellow_mug_beanie.png)

## Prerequisites
python 2.7 or higher

## Usage
```
pip install Pillow
pip install numpy
python ./main.py
```

See in/ and out/ for example