
import sys, os
from pathlib import Path

def sub_extractor(folder_path):    
    bat_file = folder_path / 'extractor.bat'
    instructions = open(bat_file,'w+')
    instructions.write('@echo off \n for /R %f IN (*.mkv) DO ffmpeg -i "%f" -map 0:s:0 "%~nf.ass" \n')


    instructions.close