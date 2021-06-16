# Batch texture compressor

![GitHub last commit](https://img.shields.io/github/last-commit/SEA-group/Batch-Texture-Compressor)
![GitHub issues](https://img.shields.io/github/issues-raw/SEA-group/Batch-Texture-Compressor)

A script that generates a "Compressed Texture Mod" by one click; written and tested in Python 3.8.3 32-bits.

I have just learnt python last month, if you find any stupid or ugly codes here, don't hesitate to open issues or pull requests etc.

## How it works
Pillow (PIL) is able to read .dds files up to BC7, but it can't save image in .dds; Wand(ImageMagick) is capable to load and write .dds but it doesn't support BC7/DXT10. So I have to use both libraries, which can't share image data between them. Finally the idea is to use Pillow to read dds and save resized image in png, then use Wand to convert png to dds.

## Requirement and preparation
Although the tool is supposed to do all the job by just one click, it does require some additional works before the first use. 
1. Install pillow library: in cmd or powershell, type `pip install pillow`
2. Install wand library: in cmd or powershell, type `pip install wand`
3. Install ImageMagick and set envionment variable for it: please follow [this page](https://docs.wand-py.org/en/0.6.6/guide/install.html#install-imagemagick-on-windows). 
* **Attention:** The choice between ImageMagick x86 and x64 depends on your Python, not your OS. For example I have 32-bits Python on 64-bits Windows, so I must install 32-bits ImageMagick
![Screenshot]()

## How to use

It takes all .dds files in *inputDir* folder, and saves a resized copy in *outputDir* folder
