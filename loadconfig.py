#############################
#loadconfig.py
#load the config file 
#############################
import json

class LoadConfig():
    """this is the moudle load the param from config file"""
    def __init__(self,file_name):
        self.file_name=file_name
        self.config_param=None
        self.__loadParam__(file_name)
    
    def __loadParam__(self,file_name):
        try:
            with open(file_name) as config_file:
                # try:
                    config_param=json.load(config_file)
                # except json.decoder.JSONDecodeError:
                    # raise(Exception('please use json format in '+str(file_name)))
        except FileNotFoundError:
            raise(Exception('the file '+str(file_name)+' not exist!!!'))
        else:
            self.config_param=config_param
    
    def getLoadFile(self):
        return self.config_param['loadfile']

    def getDimensions(self):
        dimensions=[]
        dimensions.append(self.config_param['dimensions']['z'])
        dimensions.append(self.config_param['dimensions']['y'])
        dimensions.append(self.config_param['dimensions']['x'])
        dimensions.append(self.config_param['dimensions']['b'])
        dimensions.append(self.config_param['dimensions']['c'])
        dimensions.append(self.config_param['dimensions']['a'])
        return dimensions

    def getRouteName(self):
        return self.config_param['route']['name']

    def getRouteUsedLinks(self):
        return self.config_param['route']['usedlinks']

    def getLocaterName(self):
        return self.config_param['locater']['name']

    def getLocaterLocation(self):
        return self.config_param['locater']['location']

    def getOffset(self):
        return self.config_param['offset']

    def getOutputPath(self):
        return self.config_param['outputpath']

    def getOpticalWeight(self):
        return self.config_param['route']['opticalweight']
    
    def getOpticalMapperName(self):
        return self.config_param['opticalconnectmapper']



# loadconfig=LoadConfig('config\configure.txt')
# print(loadconfig.getLoadFile())
# print(loadconfig.getDimensions())
# print(loadconfig.getLocaterLocation())
# print(loadconfig.getLocaterName())
# print(loadconfig.getOffset())
# print(loadconfig.getRouteName())
# print(loadconfig.getRouteUsedLinks())
# print(loadconfig.getOpticalWeight())

# out={"file":"out\\123.txt"}
# print("out/123.txt")
# print("out\\123.txt")
# print(json.dumps(out))


