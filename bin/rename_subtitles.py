#!/usr/bin/env python3

import os, stat
import re
import shutil

# define the name of the directory to be created
path = "./Subs"

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

if (os.path.isdir(path)):
    shutil.rmtree(path, onerror=remove_readonly)

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)

# os.rename(r'file_name_old_01.txt', r'file_name_new_01.txt')
video_file_ext = ['.mkv',
                 '.mp4',
                 '.m4v',
                 '.m4p',
                 '.wmv',
                 '.flv',
                 '.f4v',
                 '.f4p',
                 '.f4a',
                 '.f4b']

subtitles_file_ext = ['.srt',
                      '.lrc',
                      '.ttml',
                      '.ccml',
                      '.ttxt',
                      '.mp4tt',
                      '.sami',
                      '.ssa',
                      '.smil',
                      '.usf',
                      '.sub']

file_list = []
subtitles_file_list = []
video_file_list = []
file_list = os.listdir('.')
# for root, files in os.walk("."):
#     for filename in files:
#         print(filename)
#         file_list.append(filename)

for file in file_list:
    for extension in subtitles_file_ext:
        if file.endswith(extension):
            ext = file.split(extension)
            subtitles_file_list.append(ext[0])
            if (len(ext) > 2):
                os.rename(file, ext[0] + extension)

    for extension in video_file_ext:
        if file.endswith(extension):
            ext = file.split(extension)
            video_file_list.append(ext[0])

print("\n")

print("subtitles_file_list:")
for file in subtitles_file_list:
    print(file)
print("\n")

print("video_file_list:")
for file in video_file_list:
    print(file)
print("\n")

for file_x in subtitles_file_list:
    x = re.findall('[eE]\d{2}', file_x)
    print(x[0])
    z = str(x[0])
    k = z[1:3]
    print(k)
    #it is TV show
    if x:
        for file_y in video_file_list:
            y = re.findall('[eE]' + k, file_y)
            if y:
                os.rename(file_x + ".srt", file_y + ".srt")
                shutil.copy(file_y + ".srt", path.format(os.path.basename(file_y)))
    #it is a movie
    else:
        for file_y in video_file_list:
            os.rename(file_x + ".srt", file_y + ".srt")
            shutil.copy(file_y + ".srt", path.format(os.path.basename(file_y)))

print("Final file list:")
file_list = os.listdir('.')
for file in file_list:
    print(file)

input('Press Enter to Continue...')