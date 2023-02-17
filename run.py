import json
import os


def make_dirs(data):
    #  create directories 
    for k, v in data.items():
        if isinstance(v, dict): 
            os.makedirs(k, exist_ok=True)
            os.chdir(os.getcwd()+'/'+k)
            make_dirs(v) 
        else:
            os.makedirs(k, exist_ok=True)
            print(os.getcwd()) 

# load json file tree.json
j_file = "tree.json"
with open(j_file, 'r', encoding='utf-8') as jf:
    data = json.load(jf)
    make_dirs(data)
