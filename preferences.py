EXIFTOOL_PATH = "/usr/local/bin/exiftool"

ORIGINAL_FILE_EXTENSIONS = ["mp4", "mov"]
COMPRESSED_FILE_EXTENSIONS = ["mp4", "mov"]  # Compressed file extensions to look for
COMPRESSED_MARKER = " (HEVC)"  # Extra text marker in compressed filename. Usage: FILENAME + COMPRESSED_MARKER + EXTENSION (example: "IMG_009.MP4" >> "IMG_009 (HEVC).MOV")
