from urllib import request
import os
import zipfile
import shutil
import time
import sys

URL = 'https://github.com/ysenarath/TweetToolkit/releases/download/v0.1/Ark-TweetNLP.zip'
ROOT_FOLDER = 'tools'

def reporthook(count, block_size, total_size):
    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r- %d%%, %d MB, %d KB/s, %d seconds passed" %
     (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()


def download(url=URL, root=ROOT_FOLDER):
    if os.path.exists(root):
        if input('- Folder with the same name exist. '
        'Do you want to delete that and download the files again? [y/N] ').lower() == 'y':
            shutil.rmtree(root)
        else:
            return
    zip_file = os.path.join(root, 'tools.zip')
    if not os.path.exists(root):
        os.makedirs(root)
    request.urlretrieve(url, zip_file, reporthook)
    with zipfile.ZipFile(zip_file, 'r') as zf:
        zf.extractall(root)
    os.remove(zip_file)


if __name__ == "__main__":
    download()