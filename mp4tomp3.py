# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 00:28:56 2022

@author: AK Nahin
"""
#!/usr/bin/env python3.7

import os
from moviepy.editor import *

e = None
while e !='y' and e!='n':
    vdo = input("Give your video file name only (without .mp4 extension): ")+'.mp4'
    vdopath = input("Give video file full path: ")
    adoname = input("Give your mp3 file name (without .mp3 extension): ")+'.mp3'
    c = None
    while c!='y' and c!='n':
        c = input("do you want to save audio file in the same directory? y/n ")
        if c == 'n':
            adopath = input("Put the full path here: ")
        elif c == 'y':
            adopath = vdopath
        else:
            print("you put a wrong input")
    video = VideoFileClip(os.path.join(vdopath,vdo))
    video.audio.write_audiofile(os.path.join(adopath,adoname))
    e = input("do you want to convert another mp4 to mp3? y/n ")
input("press enter to exit")