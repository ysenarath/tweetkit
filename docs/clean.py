import os
import shutil

html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_build', 'html')


def clean():
    """cleans the build."""
    for file in os.listdir(html_path):
        if file == '.git' or file == '.gitignore' or file == '.nojekyll':
            continue
        path = os.path.join(html_path, file)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)


if __name__ == '__main__':
    clean()
