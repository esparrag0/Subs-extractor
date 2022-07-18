import sys, subprocess
from pathlib import Path

folder_path = sys.argv[1]   
bat_file = Path(folder_path) / 'extractor.bat'
instructions = open(bat_file,'w+')
instructions.write('@echo on \nfor /R %%f IN (*.mkv) DO ffmpeg -i "%%f" -map 0:s:0 "%%~nf.ass" \npause')
instructions.close()
subprocess.call(bat_file)