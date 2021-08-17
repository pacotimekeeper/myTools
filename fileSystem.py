from os import listdir as ls, getcwd as pwd
from os.path import join as joinpath, dirname, isdir, isfile, basename

__all__ = ['ls',
           'pwd',
           'dirname',
           'joinpath',
           'allFiles',
           'isdir',
           'isfile',
           'basename']

def allFiles(dir: str = pwd()):
    return [joinpath(dir, file) for file in ls(dir)]
