import sys, subprocess, os
from pathlib import Path

folder_path = Path(sys.argv[1])
os.chdir(folder_path)
bat_file = folder_path / 'extractor.bat'
instructions = open(bat_file,'w+')
instructions.write('''@echo off
for /R %%f IN (*.mkv) DO ffmpeg -i "%%f" -map 0:s:0 "%%~nf.ass" 
(goto) 2>nul & del "%~f0"''')

#Batch command for calling ffmpeg to extract the subs. The batch file will delete itself after running

instructions.close()
subprocess.call(bat_file)