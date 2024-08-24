import glob, os, sys

if len(sys.argv) > 1:
    folder = sys.argv[1]
else:
    folder = 'input_folder'

files = glob.glob(f'{folder}/*.mp4')

for f in files:
    path = f'{folder}/thumbnails/{f}'
    if not os.path.isdir(path):
        os.makedirs(path)
        os.system(f'ffmpeg -i {f} -vf fps=1 "{path}/thumb%04d.png"')
    print(f, 'done')
    
os.system('pause')