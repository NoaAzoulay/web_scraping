

import os

def create_folder(folder_name):
    path=os.getcwd()
    newpath=path.replace(os.sep, '/')
    newpath =newpath+'/'+folder_name+'/'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
