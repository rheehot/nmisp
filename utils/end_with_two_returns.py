import os

import nbformat


def get_cur_dir():
    return os.path.abspath(os.path.dirname(__file__))


def get_par_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


def gen_items(path):
    for item in os.listdir(path):
        path_item = os.path.abspath(os.path.join(path, item))
        assert os.path.exists(path_item), f"Missing : {path_item}"
        yield path_item


def gen_folders(path=get_par_dir()):
    for item in gen_items(path):
        if os.path.isdir(item):
            yield item


def gen_files(path, ext='ipynb'):
    for item in gen_items(path):
        if os.path.isfile(item):
            if os.path.splitext(item)[-1].endswith(ext):
                yield item


def gen_ipynb_files_above(path=get_par_dir(), ext='ipynb'):
    for folder in gen_folders(path):
        for file in gen_files(folder, ext):
            yield file


def gen_cells(ipynb_file):
    nb = nbformat.read(ipynb_file, nbformat.NO_CONVERT)

    for cell in nb['cells']:
        yield cell
