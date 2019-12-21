#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Omar Zidan
# DATE CREATED: 11/3/2019                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import os

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 

def get_pet_labels(image_dir):
    
    #check here
    #filename_list = listdir(image_dir)
    
    #print("\nPrints 10 filenames from folder pet_images/")
    #for idx in range(0, 40, 1):
    #      print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )
    #results_dic = dict()
    #items_in_dic = len(results_dic)
    #print("\nEmpty Dictionary results_dic - n items=", items_in_dic)
    #check ends here
    
    in_files = listdir(image_dir)
    results_dic = dict()
    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            list_word = in_files[idx].split("_")
            pet_label=""
            for list_word1 in list_word:
                if list_word1.isalpha():
                    pet_label += list_word1.lower() + " "
            pet_label=pet_label.strip()   
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
            
            
            else:
                print("** Warning: Duplicate files exist in directory:",in_files[idx])
            
            '''
            list_word = in_files[idx].lower()
            list_word2 = list_word.strip() 
            list_word1 =  os.path.splitext(list_word2)#split("_")listdir
            #list_word2 = list_word1.strip() 
            //pet_label = ""
            for word in list_word1:
                if word.isalpha():
                    pet_label += word + " "
                    
                    
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label.strip()] # [idx] excluded
            ''' 
            
            
    
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
