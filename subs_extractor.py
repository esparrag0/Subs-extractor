import sys, subprocess, os
from pathlib import Path

folder_path = Path(sys.argv[1])
os.chdir(folder_path)
bat_file = folder_path / 'extractor.bat'
instructions = open(bat_file,'w+')
instructions.write('''@echo off
for /R %%f IN (*.mkv) DO ffmpeg -i "%%f" -map 0:s:0 "%%~nf.ass" 
(goto) 2>nul & del "%~f0"''')
instructions.close()
subprocess.call(bat_file)