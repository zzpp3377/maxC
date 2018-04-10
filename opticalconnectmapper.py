
class OpticalConnectMapper:
    """this is a data struct, discribe which switch node linked by optical links"""
    def __init__(self,name):
        self.name=name
    
    def record(self,dimensions,opticalConnectMap):
        print("link method")

class FarthestMapper(OpticalConnectMapper):
    """optical link connect the farthest si in torus"""
    def __init__(self,name):
        super().__init__(name)
    
    def record(self,dimensions,opticalConnectMap):
        for i in range(0,dimensions[0]):
            for j in range(0,dimensions[1]):
                for k in range(0,dimensions[2]):
                    key=(i,j,k)
                    value=[-1,-1,-1]
                    value[0]=(i+dimensions[0]//2+dimensions[0]%2)%dimensions[0]
                    value[1]=(j+dimensions[1]//2+dimensions[1]%2)%dimensions[1]
                    value[2]=(k+dimensions[2]//2+dimensions[2]%2)%dimensions[2]
                    if key in opticalConnectMap.keys():
                        raise Exception("a optical links can only links two switch node!!!")
                    else:
                        opticalConnectMap[key]=value


     
        # print(self.name)
        # for i in range(0,dimensions[0]):
        #     for j in range(0,dimensions[1]):
        #         for k in range(0,dimensions[2]):
        #             key=(i,j,k)
        #             value=opticalConnectMap[key]
        #             print(str(key)+"<-->"+str(value))


                 
                

        

