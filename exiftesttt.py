original_path = '/Volumes/AH_DISK5_PICS/PHOTOS & VIDEOS/Mavic Air/2020_12/102MEDIA/DJI_0984.MP4'
compressed_path = '/Volumes/AH_DISK5_PICS/PHOTOS & VIDEOS/Mavic Air/2020_12/102MEDIA/HEVC (compressed)/DJI_0984-HEVC-20201228-102100.m4v'



import subprocess
import os
import os.path
from os import path
import json

import time
import datetime

class ExifTool(object):

    sentinel = "{ready}\n"

    def __init__(self, executable="/usr/local/bin/exiftool"):
        self.executable = executable

    def __enter__(self):
        self.process = subprocess.Popen(
            [self.executable, "-stay_open", "True",  "-@", "-"],
            universal_newlines=True,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        return self

    def  __exit__(self, exc_type, exc_value, traceback):
        self.process.stdin.write("-stay_open\nFalse\n")
        self.process.stdin.flush()

    def execute(self, *args):
        args = args + ("-execute\n",)
        self.process.stdin.write(str.join("\n", args))
        self.process.stdin.flush()
        output = ""
        fd = self.process.stdout.fileno()
        while not output.endswith(self.sentinel):
            output += os.read(fd, 4096).decode('utf-8')
        return output[:-len(self.sentinel)]

    def get_metadata(self, *filenames):
        return json.loads(self.execute("-G", "-j", "-n", *filenames))

"""
with ExifTool() as e:
    metadata = e.get_metadata(original_path)
    print(metadata)
"""




EXIFTOOL = '/usr/local/bin/exiftool'
DIRPATH = "/Volumes/AH_DISK5_PICS/PHOTOS & VIDEOS/Mavic Air/2020_08/101MEDIA"

# read the entries
with os.scandir(DIRPATH) as fileList:
    
    for file in fileList:
        fileName = file.name
        filePath = file.path
        #fileStat = file.stat()

        fileNameSplit = fileName.split('.')
        fileNameName = '.'.join( fileNameSplit[:-1] )
        fileExtension = fileNameSplit[-1]

        # Skip iteration if not movie
        if fileExtension.lower() not in ('mp4'):
            continue

        #print(f'\nProcessing {fileName}')

        with ExifTool() as e:
            metadata = e.get_metadata(filePath)
        fileModifyDate = metadata[0]['File:FileModifyDate']

        #fileModifyDate = fileModifyDate[:-6]

        HEVCDirPath = DIRPATH + '/HEVC (compressed)/'
        HEVCFileName = fileNameName + '-Apple Devices 4K (HEVC 8-bit).m4v'
        HEVCFilePath = HEVCDirPath + HEVCFileName

        if not path.exists(HEVCFilePath):
            print(f'{HEVCFilePath} not found')
            continue

        #os.system(f'exiftool -AllDates="{fileModifyDate}" {HEVCFilePath}')
        #print(f'exiftool -AllDates="{fileModifyDate}" "{HEVCFilePath}"')

        
        process = subprocess.Popen(
            [
                '/usr/local/bin/exiftool',
                f'-AllDates={fileModifyDate}',
                '-overwrite_original',
                HEVCFilePath
            ],
            stdin=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )
        

        stdout, stderr = process.communicate()
        #print(stdout, stderr)

        # CHANGE FILE MODTIME
        date_time_obj = datetime.datetime.strptime(fileModifyDate, '%Y:%m:%d %H:%M:%S%z')
        modTime = time.mktime(date_time_obj.timetuple())
        os.utime(HEVCFilePath, (modTime, modTime))










