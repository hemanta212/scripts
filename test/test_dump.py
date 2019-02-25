import os
def read(self, key=None, value=None, keys=False, values=False):
        '''
        Reads and return key or value from config file
        Params:
           [o] key: Key of dictionary to get the value of
           [o] value : value of dictionary to get key of
           [o] keys [bool] : True returns all keys in list
           [o] values [bool]: True returns all values in list
           get() only will return full dictionary object
        '''
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r')as rf:
                json_data = rf.read() 
                content = json.loads(json_data) 
                if values or keys and key  or value:
                    print("Use of multiple option prohibited")
                    return('mutiple arguments error')
                elif key and value is None: 
                        value = content[key]
                        return value
                    except KeyError as e:
                        print(e,"no such key")
                        return 'keyerror'
                elif value and key is None: 
                    try:
                        value = [k for k,v in a.items() if v==value]
                        return value
                    except KeyError as e:
                        print(e,"no such key")
                        return 'keyerror'

                elif not value and not key and not keys and not values 
                    return content 

        else:
            print("File not found")
            return 'file not found'

def file_exists(self):
    if os.path.exists(self.file_path):
        return True
    else:
        raise FileNotFoundError("{0} file not found".format(self.file_path))

def get_dict(self):
    with open(self.file_path, 'r')as rf:
        json_data = rf.read() 
        try:
            content = json.loads(json_data) 
            return content
        except Exception as e:
            raise e("file cannot be read by json")

 def read(self, key=None, value=None, all_keys=False, all_values=False):
        '''
        Reads and return key or value from config file
            (returns config dict if no parameter)
        Params:
           [o] key: Key of dictionary to get the value of
           [o] value : value of dictionary to get key of
           [o] all_keys [bool] : True returns all keys dict object 
           [o] all_values [bool]: True returns all values dict object.
        '''
    #Check if more than 1 kwargs given           
    args = (key, value, all_keys, all_values)
    given = [1 for i in args if i]
    if len(given) >=2:
        raise ValueError("More than 1 arguments given")

    #ensure the file exists.
    self.file_exists():
    #load the dictionary from config
    configs = self.get_dict()
    if all_keys:
        return configs.keys()

    elif all_values:
        return configs.values()

    elif key:
        try:
            return configs[key]
        except KeyError:
            raise KeyError("The key doesnot exist in config")

    elif value:
        try:
            key = [k for k,v in configs.items() if v==value]
            return value[0]
        except KeyError:
            raise KeyError("The value doesnot exist in config")
    else:
        return self.get_dict()
