#! /usr/bin/env python3
# coding:utf-8

import copy
import math
import os
import sys
from shutil import copytree, ignore_patterns, rmtree
from PIL import Image as pimage
from wand.image import Image as wimage

#################### Set Parameters ####################

# Set input and output paths
inputDir = 'res_unpack'
outputDir = 'res_mods_compressed'

# Demagnification factor (e.g. if set to 4, a 1024*1024 image will be resized to 256*256)
# !!! Use power of 2 !!!
demultiplier = 8

# Minimum border length of resized image, in pixel.
# !!! Use power of 2 !!!
minBorderLength = 64

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

def rm_emptyfolder(path):
    ''' Borrowed from https://www.programmersought.com/article/46222499930/ '''
    if not os.path.exists(path):
        print ( '{0} does not exist in the directory' .format (path))
        return
    for root, dirs, files in os.walk(path, topdown=False):   
     for dir in dirs:
         if os.path.isdir(os.path.join(root, dir)):
             if (len(os.listdir(os.path.join(root, dir))) == 0):
                 os.rmdir(os.path.join(root, dir))

#################### Main program ####################

# Check folder existence
if not os.path.exists(inputDir):
    print('Incorrect input path')
    sys.exit() 
if os.path.exists(outputDir):
    rmtree(outputDir)
copytree(inputDir, outputDir, ignore=ignore_patterns('*.*', 'lods'))

# Parse dds files
fileList = listDdsFiles(inputDir)
for fileObj in fileList:
    rawPath = fileObj[len(inputDir):len(fileObj)]
    outputFile = outputDir + rawPath
    tempFile = outputDir + rawPath.replace('.dds', '.png')
    inputFile = copy.deepcopy(fileObj)
    print('Attempt to convert' + rawPath)
    saveResizedImage(inputFile, tempFile, outputFile)
    print('Successfully converted' + rawPath)

# Clean empty folders
rm_emptyfolder(outputDir)
