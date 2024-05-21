from pathlib import Path

# New directories:
img_dir = Path("path/to/downloads/Images")   # For images (.png, .jpg, .jpeg, .svg, .gif)
audio_video_dir = Path("path/to/downloads/Audios & Videos")   # For audio and video (.mp3, .mp4)
exe_dir = Path("path/to/downloads/Executable Files")   # For programs (.exe)
doc_dir = Path("path/to/downloads/Documents")   # For documents (.pdf, .doc, .docx, .txt, .pptx, .xlsx)
zip_dir = Path("path/to/downloads/Zip Files")   # For zip files (.zip)
dir_dir = Path("path/to/downloads/Existing Folders")   # For other folders (no file extension)
misc_dir = Path("path/to/downloads/Miscellaneous")   # For other file extensions (eg .html, .webp, .ini)

dir_set = {img_dir, audio_video_dir, exe_dir, doc_dir, zip_dir, dir_dir, misc_dir}

for new_dir in dir_set:
    new_dir.mkdir(exist_ok=True)

for item in downloads_dir.iterdir():
    if item.is_dir() and item not in dir_set:   # Excludes the manually made directories
        item.rename(dir_dir / item.name)
    elif item.is_file():
        file_extension = item.suffix.lower()
        if (file_extension == '.png' or file_extension == '.jpg'
                or file_extension == '.jpeg' or file_extension == '.svg' or file_extension == '.gif'):
            item.rename(img_dir / item.name)
        elif file_extension == '.mp3' or file_extension == '.mp4':
            item.rename(audio_video_dir / item.name)
        elif file_extension == '.exe':
            item.rename(exe_dir / item.name)
        elif (file_extension == '.pdf' or file_extension == '.doc' or file_extension == '.docx'
              or file_extension == '.txt' or file_extension == '.pptx' or file_extension == '.xlsx'):
            item.rename(doc_dir / item.name)
        elif file_extension == '.zip':
            item.rename(zip_dir / item.name)
        else:
            item.rename(misc_dir / item.name)
