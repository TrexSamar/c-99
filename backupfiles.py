import os
import shutil
import time

def main():
    deletedFolderCount = 0
    deletedFilesCount = 0
    path = '/'
    days = 30
    seconds = time.time()-(days*24*60*60)
    
    if os.path.exists(path):
        for rootFolder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(rootFolder):
                remove_folder(rootFolder)
                deletedFolderCount += 1
                break
            else:
                for folder in folders: 
                    folder_path = os.path.join(rootFolder, folder)     
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFolderCount += 1
                for file in files:
                    file_path = os.path.join(rootFolder, file)
                     if seconds >= get_file_or_folder_age(file_path):
                         remove_file(file_path)
                         deletedFilesCount += 1
    print(f'Totalfolders deleted: {deletedFolderCount} ')
    print(f'Totalfolders deleted: {deletedFilesCount} ')

def remove_folder(path):
    if not shutil.rmtree(path):
        print('Path removed successfully')
    else:
        print('Unable to delete path')

def remove_file(path):
    if not os.remove(path): 
        print('Path removed successfully')
    else:
        print('Unable to delete path')

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()

    