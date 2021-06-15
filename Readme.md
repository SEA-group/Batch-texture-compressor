# Batch texture compressor

![GitHub last commit](https://img.shields.io/github/last-commit/SEA-group/Batch-Texture-Compressor)
![GitHub issues](https://img.shields.io/github/issues-raw/SEA-group/Batch-Texture-Compressor)

A script that generates a "Compressed Texture Mod" by one click

I have just learnt python last month, if you find stupid codes in my script don't hesitate to open issues...

## Requirement and preparation
Although the tool is supposed to do all the job by just one click, it does require some additional works before the first use. 

Pillow (PIL) is able to read .dds files up to BC7, but it can't save image in .dds; Wand(ImageMagick) is capable to load and write .dds but it doesn't support BC7/DXT10. So I have to use both libraries.

## How to use