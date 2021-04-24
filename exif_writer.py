import os
import subprocess
import time
import datetime

from preferences import *
from errors import *
from exiftool import ExifTool


def rebuild_dirpath(dirpath: str):
    if dirpath [-1] != '/':
        dirpath += '/'
    return dirpath


def edit_metadata(original_files_path: str, compressed_files_path: str):

    # Rebuild paths
    original_files_path = rebuild_dirpath( original_files_path )
    compressed_files_path = rebuild_dirpath( compressed_files_path )


    original_files = dict()
    # Run through original files
    with os.scandir( original_files_path ) as file_list:

        for file in file_list:

            filename_full = file.name
            filepath = file.path
            filename, extension = os.path.splitext( filename_full )

            # Skip iteration if wrong extension
            if extension.lower() [1:] not in ORIGINAL_FILE_EXTENSIONS:
                continue
            
            # Write to dictionary (overwrite any previous filename)
            original_files[filename] = filepath


    # Run through compressed files
    with os.scandir( compressed_files_path ) as file_list:

        for file in file_list:
        
            filename_full = file.name
            filepath = file.path
            filename, extension = os.path.splitext( filename_full )

            # Skip iteration if wrong extension
            if extension.lower() [1:] not in COMPRESSED_FILE_EXTENSIONS:
                continue

            # Create original filename
            filename_original = filename.split( COMPRESSED_MARKER ) [0]

            # Retrieve original file extension
            try:
                filepath_original = original_files [filename_original]
            except KeyNotFoundError:
                print(f'{filename_full} - {ERROR_ORIGINAL_NOT_FOUND}')
                continue

            # Retrieve original file's creation date
            with ExifTool() as e:
                metadata = e.get_metadata( filepath_original )
                modify_date = metadata [0] ['File:FileModifyDate']
                # Here can retrieve more metadata to later write using subprocess

            # Edit compressed file's EXIF creation date
            process = subprocess.Popen(
                [
                    EXIFTOOL_PATH,
                    f'-AllDates={modify_date}',
                    '-overwrite_original',
                    filepath
                ],
                stdin=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE
            )
            stdout, stderr = process.communicate()

            # Change file's modification time
            date_time_obj = datetime.datetime.strptime(modify_date, '%Y:%m:%d %H:%M:%S%z')
            mod_time = time.mktime( date_time_obj.timetuple() )
            os.utime(filepath, (mod_time, mod_time))

    return True
