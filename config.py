'''
config_writer file to quickly write app configurations
contains:
    config_writer() #writes to ~/.cli_config.json by default
'''

import json
import os

key = "file"
value = "lodddd"
def config_writer(key, value, file='~/.cli_config.json'):
    '''
    writes to a config file as a dictionary

    params: 
        key:name of setting
        value: value of setting
        [o]file: config file path
        writes to ~/.cli_config.json by default

    Usage:
        config_writer('user.email','a@a.com',file='~/config.json')
     '''
    file_path = os.path.expanduser(file)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            print("file created")
    
    with open(file_path, 'r')as f:
        content = f.read()
        if content != "": 
            print("file is not empty. Trying to append")
            read_dict = json.loads(content)
            read_dict[key] = value
            with open(file_path, 'w')as f:
                json.dump(read_dict,f)
                print("succesfully added config")
        else: 
            with open(file_path, 'w')as f:
                print("file is empty creating first entry")
                dump_dict = {}
                dump_dict[key] = value
                json.dump(dump_dict, f)
                print("succesfully added config")
