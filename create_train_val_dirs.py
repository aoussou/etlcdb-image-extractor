import os
import glob
import random
import codecs
import shutil


###############################################################################
def create_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)


###############################################################################

path = "etl_data/images"
name = "ETL9G"
all_data_path = os.path.join(path, name)

train_path = os.path.join(path, "train")
val_path = os.path.join(path, "val")

create_dir(train_path)
create_dir(val_path)

all_folders = os.listdir(all_data_path)

for label in all_folders:
    print(label)
    dir_folder = os.path.join(all_data_path, label)

    all_images = os.listdir(dir_folder)
    n_images = len(all_images)
    val_number = int(.2 * n_images)

    val_group = random.sample(all_images, val_number)


    train_move_dir = os.path.join(train_path, label)
    create_dir(train_move_dir)
    val_move_dir = os.path.join(val_path, label)
    create_dir(val_move_dir)
    for im in all_images:

        im_path_src = os.path.join(all_data_path, label, im)

        if im in val_group:
            val_im_path_dest = os.path.join(val_move_dir, im)
            shutil.move(im_path_src, val_im_path_dest)
        else:
            train_im_path_dest = os.path.join(train_move_dir, im)
            shutil.move(im_path_src, train_im_path_dest)

    os.rmdir(dir_folder)

    #
    # for im in all_images:

os.rmdir(all_data_path)
