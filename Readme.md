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
3. Install ImageMagick **and set envionment variable** for it: please follow [this page](https://docs.wand-py.org/en/0.6.6/guide/install.html#install-imagemagick-on-windows). 
**Attention:** The choice between ImageMagick x86 and x64 depends on your Python, not your OS. For example I have 32-bits Python on 64-bits Windows, so I must install 32-bits ImageMagick
![Screenshot](https://raw.githubusercontent.com/SEA-group/Batch-Texture-Compressor/main/Installation%20instructions/ImageMagick_Installation_1.png)

## How to use
1. Make a full unpack of the dds files from the game client, to res_unpack/ for example
2. Put *Texture_Compressor.py* in WorldofWarships installation directory
3. Open *Texture_Compressor.py* with a certain text editor
4. Assign an output directory in line 16
5. Assign a denominator in line 20. 
6. Assign a minimum boarder length in line 24. The resized dds image's short boarder will not be smaller then this number.
7. Save and run *Texture_Compressor.py*. I suggest to run it by double click or in cmd/powershell, in order to avoid path problems

It takes all .dds files in `inputDir`(line16, is 'res_unpack' by default), and saves a resized copy in `outputDir`(line20)

## Warning
If `outputDir`(line20) already exists, it will be firstly removed. (Otherwise `shutil.copytree` won't work...)
