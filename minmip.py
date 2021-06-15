#! /usr/bin/env python3
# coding:utf-8

""" 
This script requires "pillow" librarie which can be installed through pip
It takes all .dds files in *inputDir* folder, and saves a resized copy in *outputDir* folder
"""

import copy
import math
import os
import sys
from shutil import copytree, ignore_patterns, rmtree
from PIL import Image as pimage
from wand.image import Image as wimage

#################### Set Parameters ####################

# Set input and output paths
inputDir = 'Input'
outputDir = 'Output'

# Demagnification factor (e.g. if set to 4, a 1024*1024 image will be resized to 256*256)
# !!! Use power of 2 !!!
demultiplier = 8

# Minimum border length of resized image, in pixel.
# !!! Use power of 2 !!!
minBorderLength = 8

#################### Functions ####################

def getExtension(path): 
  return os.path.splitext(path)[1]

def listDdsFiles(path):
    fileList=[]
    for root,dirs,files in os.walk(path):
        for fileObj in files:
            if getExtension(fileObj) == '.dds':
                fileList.append(os.path.join(root,fileObj))
    return fileList

def saveResizedImage(inputFile, tempFile, outputFile):
    with pimage.open(inputFile) as inputImage:
        inputImage.load()
        if min(inputImage.size) > minBorderLength:
            if min(inputImage.size)/demultiplier < minBorderLength:
                demul = 2 ** int(math.log(min(inputImage.size)/minBorderLength) / math.log(2))
            else:
                demul = copy.deepcopy(demultiplier)
            newSize = int(inputImage.size[0]/demul), int(inputImage.size[1]/demul)
            inputImage = inputImage.resize(newSize)
        # Save temporary file
        inputImage.save(tempFile)
    with wimage(filename = tempFile) as img:
        img.options['dds:mipmaps'] = '0'
        img.compression = 'dxt5'
        img.save(filename = outputFile)
    os.remove(tempFile)

#################### Main program ####################

# Check folder existence
if not os.path.exists(inputDir):
    print('Incorrect input path')
    sys.exit() 
if os.path.exists(outputDir):
    rmtree(outputDir)
copytree(inputDir, outputDir, ignore=ignore_patterns('*.*', 'lods'))

""" with pimage.open('IAF007_Re_2000_n.dds') as inputImage:
    inputImage.load()
    print(inputImage.format, inputImage.size, inputImage.mode)
    # print(inputImage.pixel_format)
    print(inputImage.getpixel((0, 0))[0])
    print(type(getColorMap(inputImage))) """
    
fileList = listDdsFiles(inputDir)
for fileObj in fileList:
    rawPath = fileObj[len(inputDir):len(fileObj)]
    outputFile = outputDir + rawPath
    tempFile = outputDir + rawPath.replace('.dds', '.png')
    inputFile = copy.deepcopy(fileObj)
    print('Attempt to convert' + rawPath)
    saveResizedImage(inputFile, tempFile, outputFile)
    print('Successfully converted' + rawPath)
