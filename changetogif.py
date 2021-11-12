import sys, os, shutil
from os import path
from ffmpy import FFmpeg

def main(filenames):
    title, ext = os.path.splitext(os.path.basename(filenames))
    ff = FFmpeg(
        inputs = {filenames: None},
        outputs = {title + ".gif": None}
    )
    ff.run()
    os.makedirs('Finish', exist_ok = True)
    shutil.move(title + '.mp4', os.path.join('Finish'))

if __name__ == '__main__':
    filenames = sys.argv[1:]
    for value in filenames:
        main(value)