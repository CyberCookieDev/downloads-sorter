
from pathlib import Path
import os
import shutil

# All folder names/types

folders = ['Images', 'Documents', 'Ebooks', 'Videos', 'Audio', 'Programs', 'Fonts', 'Code',
           'Archive', 'Other']

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
if ask_if_custom in ['downloads', 'custom']:
    if ask_if_custom == 'downloads':
        custom = False
    else:
        custom = True
if custom == False:
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

# For loop to sort and then transfer files into correct folders.

for file in downloads_list:
    split_tup = os.path.splitext(file)
    extension = split_tup[1]
    extension = extension.replace('.', '')
    if not os.path.isdir(str(downloads_path + '/' + file)):
        if extension.lower() in code_extensions:
            shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + 'Code'))
        elif extension.lower() in ebook_extensions:
            shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + 'Ebooks'))
        elif extension.lower() in audio_extensions:
            shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + 'Audio'))
        elif extension.lower() in image_extensions:
            shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + 'Images'))
        elif extension.lower() in document_extensions:
            shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + 'Documents'))
        elif extension.lower() in program_extensions:
            shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + 'Programs'))
        elif extension.lower() in video_extensions:
            shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + 'Videos'))
        elif extension.lower() in font_extensions:
            shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + 'Fonts'))
        elif extension.lower() in archive_extensions:
            shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + 'Archive'))
    else:
        os.mkdir(str(Path.home() / "Downloads" / 'File Duplicates'))
        shutil.move(str(downloads_path + '/' + file), str(downloads_path + '/' + 'File Duplicates'))
# Gotta check if file is not in one of the created folders and possibly remove dupes