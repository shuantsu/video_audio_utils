import os, glob, sys

command = 'ffmpeg -i "%s" -q:a 0 -map a "%s"'

if len(sys.argv) > 1:
    folder = sys.argv[1]
else:
    folder = 'input_folder'

for file in glob.glob(folder + '/*.mp4'):
    output_file_path = file.replace('mp4', 'mp3')
    os.system(command % (file, output_file_path))