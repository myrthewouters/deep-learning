import pandas as pd
from os import listdir, mkdir, rename, makedirs
from os.path import isfile, join, isdir
import sys
import cv2

YOUR_PATH = '../rsna-bone-age/'

# Add filename to dataframes
def add_filename(df):
  # Create extra column in df to save path to resized and padded image
  df['img_path'] = None

  for index, row in df.iterrows():
    # Add filename to df
    filename = '{}.png'.format(index)

    # Save path to resized and padded image to df
    df.loc[index, 'img_path'] = filename

  return df

def resize_padding_img(img_path, desired_size):
    """
    Function to resize the image with padding
    Code for the resize and padding function was taken from: 
    https://jdhao.github.io/2017/11/06/resize-image-to-square-with-padding/
    """    
    im = cv2.imread(img_path)
    old_size = im.shape[:2] # old_size is in (height, width) format

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    # new_size should be in (width, height) format

    im = cv2.resize(im, (new_size[1], new_size[0]))

    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)

    color = [0, 0, 0]
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

    return new_im

def resize_padding_set(df, img_dir, img_set, desired_size):
    """
    Function to resize the entire set of images with padding and save to a desired path
    """
    # Create directory for resized and padded images
    dirname = YOUR_PATH + 'resized_padded/{}'.format(img_set)
    makedirs(dirname)
    
    for index, row in df.iterrows():
        # Resizing and padding
        img_path = img_dir + row['img_path']
       
        rp_img = resize_padding_img(img_path, desired_size)
        
        # Write resized and padded images to disk
        filename = '{}.png'.format(index)    
        
        cv2.imwrite(dirname + '/' + filename, rp_img) 
        
    return df

def resize_padding():
  # Load data, split to train and validaiton sets
  train = pd.read_csv(YOUR_PATH+'boneage-training-dataset.csv', index_col='id')
  test = pd.read_csv(YOUR_PATH+'boneage-test.csv', index_col='id')

  # Add filenames
  train = add_filename(train)
  test = add_filename(test)

  # Resizing and padding
  train = resize_padding_set(train, YOUR_PATH+'boneage-training-dataset/', 'training', 256)
  test = resize_padding_set(test, YOUR_PATH+'boneage-test-dataset/','test', 256)

  # Save train and validation sets as csv files
  train.to_csv(YOUR_PATH + 'train.csv')
  test.to_csv(YOUR_PATH + 'test.csv')

  print('Finished resizing and padding.')
  print('Images are saved in {}resized_padded'.format(YOUR_PATH))

if __name__=='__main__':
  resize_padding()
