# video-backup-utility v1.0
<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="Creative Commons Licence" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License</a>.

<br>

This program manages editing metadata for backupped files.
This program was built and tested using macOS 11.2 Big Sur and should work on all macOS and OSX versions. Compatibility with other operating systems is likely but not guaranteed. For more information, search for utility paths and subprocess syntax on your OS.

<br>

## Requirements
* <a href="https://exiftool.org" target="_blank">ExifTool</a> (reference the install path in `preferences.py > EXIFTOOL_PATH`)
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> (tested with Python 3.9.0, should work with Python 3.6.0 and newer)

<br>

## Usage
* Clone the git repository (using `git clone https://github.com/ahernot/video-backup-utility/` or a GUI such as <a href="https://desktop.github.com" target="_blank">GitHub Desktop</a>
* Open the `~/video-backup-utility/preferences.py` file (using an IDE such as <a href="https://www.python.org/downloads/" target="_blank">IDLE</a> or <a href="https://code.visualstudio.com/download" target="_blank">VSCode</a>) and reference the following preferences:
  * The ExifTool utility path (default for macOS is "/usr/local/bin/exiftool"). It should be given to you during the install process, or you can find it online.
  * The file extensions (in lowercase) for original and target files
  * The text string which is appended to a target file's name (example: ORIGINAL="IMG_009.MP4" >> COMPRESSED="IMG_009 (HEVC).MP4"). There must be no text placed between the marker (" (HEVC)" here) and the extension (".MP4" here). The filename before the marker ("IMG_009" here) must be the same as that of the original file. The marker is case-sensitive. (" (hevc)" wouldn't work here).
* Open the `~/video-backup-utility/main.py` file and reference the directory paths:
  * The path of the folder containing the original files, the metadata of which you wish to copy over to their compressed/backupped counterparts (example: `"ahernot/desktop/original/"`)
  * The path of the folder containing the compressed/backupped files (example: `"ahernot/desktop/compressed/"`)
* Open a terminal window, and run `cd PATH_TO_CLONED_FOLDER` where `PATH_TO_CLONED_FOLDER` is something like `~/video-backup-utility/`
* Run `python main.py`
