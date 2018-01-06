import json

class LoadConfig():
    """this is the moudle load the param from config file"""
    def __init__(self,file_name):
        self.file_name=file_name

    def loadParam(self):
        try:
            with open(self.file_name) as config_file:
                try:
                    config_param=json.load(config_file)
                except json.decoder.JSONDecodeError:
                    raise(Exception('please use json format in '+str(self.file_name)))
        except FileNotFoundError:
            raise(Exception('the file '+str(self.file_name)+' not exist!!!'))
        else:
            return config_param
    
    def 

# loadconfig=LoadConfig('config\configure.txt')
# config_param=loadconfig.loadParam()
# print(config_param['zp'])
# print(config_param['son']['age'])
