import os
import shutil

system_path = r"C:\Users\chl\Desktop\5.21"
new_folder_path = r'\tiny-imagenet-200\val_reorg'
os.makedirs(system_path+new_folder_path)
with open(system_path+r'\tiny-imagenet-200\val\val_annotations.txt', 'r') as file:
    for line in file:
        words = line.split()
        file_to_copy_path_r = r"\tiny-imagenet-200\val"
        file_to_copy_path = f'{system_path}{file_to_copy_path_r}\images\{words[0]}'
        copy_folder = f'{system_path}{new_folder_path}\{words[1]}'
        copy_path = copy_folder + r'\images'
        # Create the new folder
        if not os.path.exists(copy_folder):
            os.makedirs(copy_folder)
            os.makedirs(copy_path)
        #copy original images
        shutil.copy(file_to_copy_path, copy_path)




