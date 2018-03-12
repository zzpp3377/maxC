###############################
#loadmoudle.py 
#load the traffic pattern file 
###############################
import re

class LoadMoudle():
    """this is the moudle which load the traffic pattern"""
    def __init__(self,filename):
        """init this moudle"""
        self.filename=filename
        self.loads=[]
        with open(self.filename) as filep:
            max_load_list=[]  
            for line in filep:
                linelist=re.split('\t',line)
                linelist.pop(-1)
                load=[]
                for element in linelist:
                    load.append(float(element))
                self.loads.append(load)
                max_load_list.append(max(load))

            max_weight=max(max_load_list)
            if max_weight==0:
                print("error: the load are all zero!!!")
                max_weight=1
            for i in range(0,len(self.loads)):
                for j in range(0,len(self.loads[i])):
                        self.loads[i][j]=self.loads[i][j]/max_weight
        
            # print(self.loads)
    
    def loadTraffic(self,src,dst):
        """load traffic"""
        return self.loads[src][dst]

    def getProcessorNum(self):
        """return the number of processor in traffic pattern file"""
        return len(self.loads)

# load_moudle= LoadMoudle("summary.log")
# # print(load_moudle.load_traffic(255,253))
# print(load_moudle.getProcessorNum())

