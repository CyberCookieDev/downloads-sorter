
from pathlib import Path
import os
import shutil
import send2trash
import re

# All folder names/types

folders = ['Images', 'Documents', 'Ebooks', 'Videos', 'Audio', 'Programs', 'Fonts', 'Code',
           'Archive',]

# All extensions to sort them to corresponding folders

code_extensions = ['c', 'class', 'cpp', 'cs', 'css', 'go', 'h', 'htaccess', 'html', 'java', 'js',
                   'json', 'kml', 'php', 'pl', 'py', 'rb', 'sql', 'swift', 'vb', 'yaml', 'ipynb']

ebook_extensions = ['epub', 'pdb', 'fb2', 'ibook', 'inf', 'azw', 'azw3', 'mobi', ]

audio_extensions = ['mp3', 'm4a', 'aac', 'oga', 'flac', 'wav', 'pcm', 'aiff']

image_extensions = ['jpg', 'jpeg', 'jif', 'jfif', 'jfi', 'png', 'gif', 'webp', 'tiff', 'tif',
                    'psd', 'raw', 'arw', 'cr2', 'nrw', 'k25', 'bmp', 'dib', 'heif', 'heic', 'ind',
                    'indd', 'indt', 'jp2', 'j2k', 'jpf', 'jpx', 'jpm', 'mj2', 'svg', 'svgz', 'ai',
                    'eps', 'pdf']

document_extensions = ['md', 'txt', 'rtf', 'ppt', 'ott', 'odt', 'ods', 'odp', 'docx', 'doc', 'csv']

program_extensions = ['bin', 'jar', 'apk', 'exe', 'msi', 'run', 'appimage', 'sh', 'fish']

video_extensions = ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4', 'm4p', 'm4v', 'avi',
                    'wmv', 'mov', 'qt', 'flv', 'swf']

archive_extensions = ['zip', '7z', 'pkg', 'rpm', 'z', 'xz']

font_extensions = ['vfb', 'pfa', 'fnt', 'vlw', 'jfproj', 'woff', 'sfd', 'pfb']

# Ask if user wants to sort downloads or custom path using some simple logic.
ask_if_custom = input('Sort downloads or some custom location? Type downloads for downloads and custom for custom. ')
custom = True
while ask_if_custom not in ['downloads', 'custom']:
    ask_if_custom = input('Sort downloads or some custom location? Type downloads for downloads and custom for custom. ')

if ask_if_custom == 'downloads':
    custom = False
else:
    custom = True

if not custom:
    downloads_path = str(Path.home() / "Downloads")
    downloads_list = os.listdir(f'{downloads_path}')
else:
    while True:
        ask_for_path = input('Enter your path to sort: ')
        if not os.path.isdir(ask_for_path):
            pass
        else:
            downloads_path = str(ask_for_path)
            downloads_list = os.listdir(f'{ask_for_path}')
            break


# Create folders, first check if they exist to not have duplicates
for folder_type in folders:

    mypath = str(f'{downloads_path}' + '/' + f'{folder_type}')
    if not os.path.isdir(mypath):

        os.mkdir(mypath)

# Whole logic behind checking if file exists, numbering it if it already exists and you want to keep it, or if you don't, sending it to trash
def replace_or_keep(folder_name, file):

    # Checks if file already exists
    if not os.path.exists(downloads_path + '/' + folder_name + '/' + file):
        shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + folder_name))
    else:
        # If it exists, it asks for input if you want to keep both, or delete the older one
        replace_keep = input(f'{file} already exist. Do you want to replace it or keep both? replace/keep: ')
        while replace_keep not in ['replace', 'keep']:
            replace_keep = input(f'{file} already exist. Do you want to replace it or keep both? replace/keep: ')

        # Logic for sending to trash
        if replace_keep == 'replace':
            send2trash.send2trash(downloads_path + '/' + folder_name + '/' + file)
            shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + folder_name))

        # Regex to detect if file has a number, for example main_script(1).py
        else:
            file_path = (downloads_path + '/' + folder_name + '/' + file)
            file_path_reversed = file_path[::-1]
            digit_search = re.search('(\d+)', file_path_reversed)
            digit_search_span = digit_search.span
            if digit_search is not None and digit_search_span == '0':
                digit_to_edit = digit_search.group()[::-1]
                digit = digit_to_edit[1:-2]
                file_name = os.rename(downloads_path + '/' + file, downloads_path + '/' + split_tup[0] + f'({digit})' + extension)
                shutil.move(file_name, downloads_path + '/' + folder_name + '/' + split_tup[0] + f'({digit})' + extension)
            else:
                os.rename(downloads_path + '/' + file, downloads_path + '/' + split_tup[0] + '(1)' + extension)
                shutil.move(downloads_path + '/' + split_tup[0] + '(1)' + extension, downloads_path + '/' + folder_name + '/' + split_tup[0] + '(1)' + extension)

# For loop to sort and then transfer files into correct folders.

for file in downloads_list:

    split_tup = os.path.splitext(file)
    extension = split_tup[1]
    extension = extension.replace('.', '')
    if extension.lower() in code_extensions:
        replace_or_keep('Code', file)

    elif extension.lower() in ebook_extensions:
        replace_or_keep('Ebooks', file)

    elif extension.lower() in audio_extensions:
        replace_or_keep('Audio', file)

    elif extension.lower() in image_extensions:
        replace_or_keep('Images', file)
    elif extension.lower() in document_extensions:
        replace_or_keep('Documents', file)

    elif extension.lower() in program_extensions:
        replace_or_keep('Programs', file)

    elif extension.lower() in video_extensions:
        replace_or_keep('Videos', file)

    elif extension.lower() in font_extensions:
        replace_or_keep('Fonts', file)

    elif extension.lower() in archive_extensions:
        replace_or_keep('Archive', file)
