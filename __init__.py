import pickle
import os
import sys

name="twitter_variation"
version="1.0.1"
author="Shubhanshu Sharma"

english_variation_file_path = os.path.join(os.path.dirname(__file__),'variation_to_english_dict.pickle')
with open(english_variation_file_path,'rb') as f:
    variation_dict = pickle.load(f)

def variation_to_english(sent=''):
    for k,v in variation_dict.items():
        sent = sent.replace(k,v)
    if sys.version_info[0]<3:
        return sent.encode()
    return sent
