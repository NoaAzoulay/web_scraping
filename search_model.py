
import os


# enter string, path and folder-name to search the string in all files in folder
def search_string_in_files(str, folder_name, path):
    path = path
    new = path.replace(os.sep, '/')
    new=new+"/"+folder_name+"/"
    for file_name in os.listdir(new):
        with open(new+file_name, 'r', encoding="utf-8") as inF:
            for line in inF:
                if str in line:
                    print('string exists in ' + file_name, line)
                    break
