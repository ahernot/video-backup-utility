import os
##

from preferences import *
from errors import *


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

        filename_full = file.name
        filepath = file.path
        filename, extension = os.path.splitext( filename_full )

        # Skip iteration if wrong extension
        if extension.lower() not in ORIGINAL_FILE_EXTENSIONS:
            continue
        
        # Write to dictionary (overwrite any previous filename)
        original_files[filename] = filepath


    # Run through compressed files
    with os.scandir( compressed_files_path ) as file_list:
        
        filename_full = file.name
        filename, extension = os.path.splitext( filename_full )

        # Skip iteration if wrong extension
        if extension.lower() not in COMPRESSED_FILE_EXTENSIONS):
            continue

        # Create original filename
        filename_original = filename.split[ COMPRESSED_MARKER ] [0]

        # Retrieve original file extension
        try:
            filepath_original = original_files [filename_original]
        except KeyNotFoundError:
            print(f'{filename_full} - {ERROR_ORIGINAL_NOT_FOUND}')
            continue

        # Retrieve original file's metadata
        with ExifTool() as e:
            metadata = e.get_metadata( filepath_original )
            modify_date = metadata [0] ['File:FileModifyDate']












    
    with os.scandir(DIRPATH) as file_list:

        for file in fileList:
            file_name_full = file.name
            file_path = file.path
            #fileStat = file.stat()

            file_name, file_extension = os.path.splitext( file_name_full )

            # Skip iteration if not movie
            if file_extension.lower() not in ('mp4'):
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
