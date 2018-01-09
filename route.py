from path import Path

class Route():
    """this is the route class , which define a interface routing()"""
    def __init__(self,name):
        self.name=name

    def routing(self,src,dst,load,topo_swports):
        print("routes from "+str(src)+" to "+str(dst))

class Dor(Route):
    """this is the dor route class"""
    def __init__(self,name,dimensions):
        super().__init__(name)
        self.dimensions=dimensions

    def routeTool(self,src,dst,load,topo_swports,path):
        """this is the dor route tool,given a source coordinate and a destination coordinate ,complete a path"""
        swport=topo_swports
        now_location=src.copy()            
        
        for i in range(len(self.dimensions)-1,-1,-1):  #i=5,4,3,2,1,0
            if dst[i]>=src[i]:              #计算在该维度上的跳数与方向
                if abs(dst[i]-src[i])<=self.dimensions[i]//2:
                    temp_src=src[i]+1
                    temp_dst=dst[i]+1
                    temp_step=1
                else:
                    temp_src=src[i]+self.dimensions[i]-1
                    temp_dst=dst[i]-1
                    temp_step=-1
            if dst[i]<src[i]:               
                if abs(dst[i]-src[i])<=self.dimensions[i]//2:
                    temp_src=src[i]-1
                    temp_dst=dst[i]-1
                    temp_step=-1
                else:
                    temp_src=src[i]+1
                    temp_dst=dst[i]+self.dimensions[i]+1
                    temp_step=1

            for j in range(temp_src,temp_dst,temp_step):
                now_location[i]=j%self.dimensions[i]
                swport=topo_swports
                for k in range(0,len(self.dimensions)):   #查找坐标now_location对应的交换机
                    swport=swport[now_location[k]]
                if i==5:                #dimension a
                    swport=swport[7]
                elif i==4:                #dimension c
                    swport=swport[8]
                elif i==3 and temp_step==1:    #dimension b+
                    swport=swport[9]
                elif i==3 and temp_step==-1:   #dimension b-
                    swport=swport[10]
                elif i==2 and temp_step==1:  #dimension x+
                    swport=swport[1]
                elif i==2 and temp_step==-1: #dimension x-
                    swport=swport[2]
                elif i==1 and temp_step==1:#dimension y+
                    swport=swport[3]
                elif i==1 and temp_step==-1:#dimension y-
                    swport=swport[4]
                elif i==0 and temp_step==1:#dimension z+
                    swport=swport[5]
                elif i==0 and temp_step==-1: #dimension z-
                    swport=swport[6]
                path.swports.append(swport) 

    def routing(self,src,dst,load,topo_swports):
        """this is the dor route algorithm,given a source coordinate and a destination coordinate ,return a path"""
        path=Path(load,self)   #this is different from chppnetsim when src==dst
        now_location=src.copy()

        swport=topo_swports
        for k in range(0,len(self.dimensions)):         
            swport=swport[src[k]]
        swport=swport[0]    #switch's port 0 connects nic 
        path.swports.append(swport)               
        
        self.routeTool(src,dst,load,topo_swports,path)               
        return path

    def getStepNum(self,src,dst):
        """given a source coordinate and a destination coordinate ,return the step number"""
        step=0
        for i in range(0,len(self.dimensions)):
            if abs(dst[i]-src[i])<=self.dimensions[i]//2:
                step=step+abs(dst[i]-src[i])
            else:
                step=step+self.dimensions[i]-abs(dst[i]-src[i])
        return step

class DorBiu(Route):
    """this is the dorbiu class"""
    def __init__(self,name,dimensions,links,optical_weight,offset):
        super().__init__(name)
        self.dimensions=dimensions
        self.links=links
        self.optical_weight=optical_weight
        self.dor=Dor('dor',dimensions)
        self.offset=offset
        self.comm_sw_map=[      #dimension order: bca;[dst_b,dst_c,dst_a,comm_b,comm_c,comm_a]
            [                   #links=12
                [0,0,0,0,0,0],
                [0,0,1,0,0,1],
                [0,1,0,0,1,0],
                [0,1,1,0,1,1],
                [1,0,0,1,0,0],
                [1,0,1,1,0,1],
                [1,1,0,1,1,0],
                [1,1,1,1,1,1],
                [2,0,0,2,0,0],
                [2,0,1,2,0,1],
                [2,1,0,2,1,0],
                [2,1,1,2,1,1]
            ],
            [                   #links=6
                [0,0,0,0,0,0],
                [0,0,1,0,0,0],
                [0,1,0,0,1,0],
                [0,1,1,0,1,0],
                [1,0,0,1,0,1],
                [1,0,1,1,0,1],
                [1,1,0,1,1,0],
                [1,1,1,1,1,0],
                [2,0,0,2,0,1],
                [2,0,1,2,0,1],
                [2,1,0,2,1,1],
                [2,1,1,2,1,1]
            ], 
            [                   #links=4
                [0,0,0,0,0,0],
                [0,0,1,0,0,1],
                [0,1,0,2,1,0],
                [0,1,1,2,1,1],
                [1,0,0,0,0,0],
                [1,0,1,0,0,1],
                [1,1,0,2,1,0],
                [1,1,1,2,1,1],
                [2,0,0,0,0,0],
                [2,0,1,0,0,1],
                [2,1,0,2,1,0],
                [2,1,1,2,1,1]
            ], 
            [                   #links=3
                [0,0,0,0,0,0],
                [0,0,1,0,0,0],
                [0,1,0,0,0,0],
                [0,1,1,2,1,1],
                [1,0,0,1,0,0],
                [1,0,1,1,0,0],
                [1,1,0,1,0,0],
                [1,1,1,1,0,0],
                [2,0,0,0,0,0],
                [2,0,1,2,1,1],
                [2,1,0,2,1,1],
                [2,1,1,2,1,1]
            ], 
            [                   #links=2
                [0,0,0,0,0,0],
                [0,0,1,0,0,0],
                [0,1,0,0,0,0],
                [0,1,1,2,1,1],
                [1,0,0,0,0,0],
                [1,0,1,0,0,0],
                [1,1,0,2,1,1],
                [1,1,1,2,1,1],
                [2,0,0,0,0,0],
                [2,0,1,2,1,1],
                [2,1,0,2,1,1],
                [2,1,1,2,1,1]
            ], 
            [                   #links=1
                [0,0,0,0,0,0],
                [0,0,1,0,0,0],
                [0,1,0,0,0,0],
                [0,1,1,0,0,0],
                [1,0,0,0,0,0],
                [1,0,1,0,0,0],
                [1,1,0,0,0,0],
                [1,1,1,0,0,0],
                [2,0,0,0,0,0],
                [2,0,1,0,0,0],
                [2,1,0,0,0,0],
                [2,1,1,0,0,0]
            ]  
            ]
        if self.links not in [12,6,4,3,2,1]:
            raise Exception('self links out of [12,6,4,3,2,1]!!!')
    
    def __getCommSw__(self,dst):
        """given a destination switch coordinate, return a communication switch coordinate"""
        result=dst.copy()
        if self.links==12:
            index=0
        elif self.links==6:
            index=1
        elif self.links==4:
            index=2
        elif self.links==3:
            index=3
        elif self.links==2:
            index=4
        elif self.links==1:
            index=5
        
        for dst2comm in self.comm_sw_map[index]:
            if dst[3:6]==dst2comm[0:3]:       #compare the coordinate in dimension b,c,a
                result[3:6]=dst2comm[3:6]
                return result
        
        raise Exception('can not find dst2comm match your input!!!')

    def __getBrotherSw__(self,comm_sw):  #related to topo ,so this method should in Topo 
        """given a communication switch coordinate, return a brother switch coordinate"""
        result=comm_sw.copy()
        if comm_sw[0]<self.dimensions[0]//2:                        
            result[0]=(result[0]+self.dimensions[0]//2+self.dimensions[0]%2)%self.dimensions[0] #dimension z
            result[1]=(result[1]+self.dimensions[1]//2+self.dimensions[1]%2)%self.dimensions[1] #dimension y
            result[2]=(result[2]+self.dimensions[2]//2+self.dimensions[2]%2-self.offset)%self.dimensions[2] #dimension x
        else:
            result[0]=(result[0]+self.dimensions[0]//2+self.dimensions[0]%2)%self.dimensions[0] #dimension z
            result[1]=(result[1]+self.dimensions[1]//2+self.dimensions[1]%2)%self.dimensions[1] #dimension y
            result[2]=(result[2]+self.dimensions[2]//2+self.dimensions[2]%2+self.offset)%self.dimensions[2] #dimension x
        return result


    def getStepNum(self,src,dst):
        """given a source coordinate and a destination coordinate, return the step number"""
        comm_sw=self.__getCommSw__(dst)
        brother_sw=self.__getBrotherSw__(comm_sw)
        step=self.dor.getStepNum(src,brother_sw)+self.optical_weight+self.dor.getStepNum(comm_sw,dst)  #the number 1 is the step on optical link
        return step

    def dorBiuRouting(self,src,dst,load,topo_swports):
        """this is the dorbiu route algorithm,given a source coordinate and a destination coordinate ,return a path"""
        path=Path(load,self)
        comm_sw=self.__getCommSw__(dst)
        brother_sw=self.__getBrotherSw__(comm_sw)

        swport=topo_swports            #nic -> source switch
        for k in range(0,len(self.dimensions)):         
            swport=swport[src[k]]
        swport=swport[0]            #switch's port 0 connects nic 
        path.swports.append(swport)
        
        self.dor.routeTool(src,brother_sw,load,topo_swports,path) #source switch -> brother switch
        
        comm_sw_port=topo_swports                           #brother switch -> communication switch
        for k in range(0,len(self.dimensions)):
            comm_sw_port=comm_sw_port[comm_sw[k]]
        comm_sw_port=comm_sw_port[11]                       #port 11 connects optical link
        path.swports.append(comm_sw_port)

        self.dor.routeTool(comm_sw,dst,load,topo_swports,path) #communication switch -> destination switch
        #to be honest, there should be a destination switch -> nic
        return path

    def routing(self,src,dst,load,topo_swports):
        """this is the combine of dor and dorbiu, choose the shortest to complete path"""
        if self.getStepNum(src,dst)<self.dor.getStepNum(src,dst):
            path=self.dorBiuRouting(src,dst,load,topo_swports)
        else:
            path=self.dor.routing(src,dst,load,topo_swports)
        return path


class Dorx(Route):
    """this is the dorx route class"""
    def __init__(self,name,dimensions,offset):
        super().__init__(name)
        self.dimensions=dimensions
        self.dor=Dor('dor',dimensions)
        self.offset=offset
        if self.offset>self.dimensions[2]//2:
            raise(Exception("offset should not bigger than half of dimension x!!!"))


    def getStepNum(self,src,dst):
        pass

    def __getBrotherSw__(self,dst):                 #related to topo ,so this method should in Topo 
        """given a destination switch coordinate, return a brother switch coordinate"""
        result=dst.copy()                                   
        if dst[0]<self.dimensions[0]//2:                        
            result[0]=(result[0]+self.dimensions[0]//2+self.dimensions[0]%2)%self.dimensions[0] #dimension z
            result[1]=(result[1]+self.dimensions[1]//2+self.dimensions[1]%2)%self.dimensions[1] #dimension y
            result[2]=(result[2]+self.dimensions[2]//2+self.dimensions[2]%2-self.offset)%self.dimensions[2] #dimension x
        else:
            result[0]=(result[0]+self.dimensions[0]//2+self.dimensions[0]%2)%self.dimensions[0] #dimension z
            result[1]=(result[1]+self.dimensions[1]//2+self.dimensions[1]%2)%self.dimensions[1] #dimension y
            result[2]=(result[2]+self.dimensions[2]//2+self.dimensions[2]%2+self.offset)%self.dimensions[2] #dimension x
        return result    
    
    def routing(self,src,dst,load,topo_swports):
        """this is the dorx route algorithm, given a source coordinate and a destination coordinate ,return a path"""        
        path=Path(load,self)
        brother_sw=self.__getBrotherSw__(dst)

        swport=topo_swports            #nic -> source switch
        for k in range(0,len(self.dimensions)):         
            swport=swport[src[k]]
        swport=swport[0]            #switch's port 0 connects nic 
        path.swports.append(swport)

        now_location=src.copy() 

        for i in range(len(self.dimensions)-1,-1,-1):  #i=5,4,3,2,1,0
            if dst[i]>=src[i]:              #计算在该维度上的跳数与方向
                if abs(dst[i]-src[i])<=self.dimensions[i]//2:
                    temp_src=src[i]+1
                    temp_dst=dst[i]+1
                    temp_step=1
                else:
                    temp_src=src[i]+self.dimensions[i]-1
                    temp_dst=dst[i]-1
                    temp_step=-1
            if dst[i]<src[i]:               
                if abs(dst[i]-src[i])<=self.dimensions[i]//2:
                    temp_src=src[i]-1
                    temp_dst=dst[i]-1
                    temp_step=-1
                else:
                    temp_src=src[i]+1
                    temp_dst=dst[i]+self.dimensions[i]+1
                    temp_step=1

            for j in range(temp_src,temp_dst,temp_step):
                swport=topo_swports
                
                if now_location==brother_sw:        # go to optical link
                    for k in range(0,len(self.dimensions)):
                        swport=swport[dst[k]]
                    swport=swport[11]               #port 11 connect optical link
                    path.swports.append(swport)
                    return path
                
                now_location[i]=j%self.dimensions[i]
                for k in range(0,len(self.dimensions)):   #查找坐标now_location对应的交换机
                    swport=swport[now_location[k]]
                if i==5:                #dimension a
                    swport=swport[7]
                elif i==4:                #dimension c
                    swport=swport[8]
                elif i==3 and temp_step==1:    #dimension b+
                    swport=swport[9]
                elif i==3 and temp_step==-1:   #dimension b-
                    swport=swport[10]
                elif i==2 and temp_step==1:  #dimension x+
                    swport=swport[1]
                elif i==2 and temp_step==-1: #dimension x-
                    swport=swport[2]
                elif i==1 and temp_step==1:#dimension y+
                    swport=swport[3]
                elif i==1 and temp_step==-1:#dimension y-
                    swport=swport[4]
                elif i==0 and temp_step==1:#dimension z+
                    swport=swport[5]
                elif i==0 and temp_step==-1: #dimension z-
                    swport=swport[6]
                path.swports.append(swport)
        return path

#dor=Dor('dor',[8,6,8,3,2,2])
# print(dor.get_step_num([0,0,0,0,0,0],[1,1,1,1,1,1]))
# print(dor.get_step_num([0,0,0,0,0,0],[7,5,7,0,0,0]))
# print(dor.get_step_num([0,0,0,0,0,0],[6,2,5,0,0,0]))
# path = dor.routing([0,0,0,0,0,0],[1,1,1,1,1,1],1)
# print(path.route.name)
# dor.routing([0,0,0,0,0,0,0],[1,1,1,1,1,1,1],1,)

# dorbiu=DorBiu('dorbiu',[8,6,8,3,2,2],3)
# comm_sw=dorbiu.__getCommSw__([1,2,3,2,0,1])
# brother_sw=dorbiu.__getBrotherSw__(comm_sw)
# print(comm_sw)
# print(brother_sw)
# step=dorbiu.getStepNum([1,2,3,2,0,1],[5, 5, 7, 2, 1, 1])
# step=dorbiu.getStepNum([1,2,3,2,0,1],[2, 5, 7, 2, 1, 1])
# print(step)



