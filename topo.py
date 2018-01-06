from swport import SwPort
from route import Route,Dor,DorBiu,Dorx
from loadmoudle import LoadMoudle
from path import Path
from locater import SmallLocater,LargeLocater,HalfLocater,QuarterLocater,NearSmallLocater,NearLargeLocater
from loadconfig import LoadConfig

class Topo():
    """the Topo class represent the topology of network"""
    
    def __init__(self,load_config):
        """this dimensions must be a 6 elements list"""
        self.paths=[]
        self.dimensions=load_config.getDimensions()
        self.routes={'dor':Dor('dor',self.dimensions),
                        'dorbiu':DorBiu('dorbiu',self.dimensions,load_config.getRouteUsedLinks(),load_config.getOffset()),
                        'dorx':Dorx('dorx',self.dimensions,load_config.getOffset())}
        self.swports=[]
        self.line_swports=[]
        self.hosts=[] 
        self.jobs=[]
        self.load_moudle=LoadMoudle(load_config.getLoadFile())
        self.locater={'SmallLocater':SmallLocater('SmallLocater'),
                        'LargeLocater':LargeLocater('LargeLocater'),
                        'HalfLocater':HalfLocater('HalfLocater',load_config.getLocaterLocation()),
                        'QuarterLocater':QuarterLocater('QuarterLocater',load_config.getLocaterLocation()),
                        'NearSmallLocater':NearSmallLocater('NearSmallLocater'),
                        'NearLargeLocater':NearLargeLocater('NearLargeLocater')
                    }
        self.load_config=load_config
        #make topo
        for i in range(0,self.dimensions[0]):    #z
            array1=[]
            self.swports.append(array1)
            for j in range(0,self.dimensions[1]):    #y
                array2=[]
                self.swports[i].append(array2)
                for k in range(0,self.dimensions[2]):    #x
                    array3=[]
                    self.swports[i][j].append(array3)
                    for l in range(0,self.dimensions[3]):    #b
                        array4=[]
                        self.swports[i][j][k].append(array4)
                        for m in range(0,self.dimensions[4]):    #c
                            array5=[]
                            self.swports[i][j][k][l].append(array5)
                            for n in range(0,self.dimensions[5]):    #a
                                array6=[]
                                self.swports[i][j][k][l][m].append(array6)
                                for p in range(0,12):       #0->nic,1->x+,2->x-,3->y+,4->y-,5->z+,6->z-,7->a,8->c,9->b+,10->b-,11->m
                                    coord=[i,j,k,l,m,n,p]
                                    sw_port=SwPort(coord)
                                    self.swports[i][j][k][l][m][n].append(sw_port)
                                    self.line_swports.append(sw_port)
                                    if p==0:
                                        self.hosts.append(sw_port)
                                    # print(self.swports[i][j][k][l][m][n][p].coord)

    def locateJobs(self,locater_name):
        """locate the job on hosts"""
        proc_num=self.load_moudle.getProcessorNum()
        self.locater[locater_name].locate(self.dimensions,self.hosts,self.swports,proc_num,self.jobs)                 
                    
    def allRoute(self,route_name):
        """according to the route algorithm and traffic pattern, init the topo matrix"""
        for job in self.jobs:
            for src in range(0,self.load_moudle.getProcessorNum()):
                for dst in range(0,self.load_moudle.getProcessorNum()):
                    coord_src=job[src].coord
                    coord_dst=job[dst].coord
                    load=self.load_moudle.loadTraffic(src,dst)
                    # print(load)
                    # print('src:'+str(coord_src)+'\tdst:'+str(coord_dst))
                    path=self.routes[route_name].routing(coord_src,coord_dst,load,self.swports)
                    self.paths.append(path)
                    # for swport in path.swports:
                        # print(swport.coord)
    
    def updatePortLoad(self,path):
        for swport in path.swports:
            # print(str(swport.port_load)+"\t:\t"+str(path.path_load))
            swport.port_load=swport.port_load+path.path_load
    
    def updateAllPortLoad(self):
        for path in self.paths:
            self.updatePortLoad(path)
        # for swport in self.line_swports:
            # print('coordinate:'+str(swport.coord)+"\tload:"+str(swport.port_load))
    def getStatistics(self):
        histogram_electric={}
        histogram_optical={}
        histogram_0load=[]
        for swport in self.line_swports:
            if swport.coord[6]!=11 : 
                if swport.port_load in histogram_electric.keys():
                    histogram_electric[swport.port_load]=histogram_electric[swport.port_load]+1
                else:
                    histogram_electric[swport.port_load]=1
            else:
                if swport.port_load in histogram_optical.keys():
                    histogram_optical[swport.port_load]=histogram_optical[swport.port_load]+1
                else:
                    histogram_optical[swport.port_load]=1
            if swport.port_load==0 :
                histogram_0load.append(swport.coord)
                # print(str(swport.coord))

        with open('output\histogram_electric.txt','w') as out_file_p:
            for key in sorted(histogram_electric.keys()):
                # print(str(key)+"\t"+str(histogram[key]))
                out_file_p.write(str(key)+"\t"+str(histogram_electric[key])+"\n")
        with open('output\histogram_optical.txt','w') as out_file_p:
            for key in sorted(histogram_optical.keys()):
                out_file_p.write(str(key)+"\t"+str(histogram_optical[key])+"\n")
        with open('output\histogram_0load.txt','w') as out_file_p:
            for coord in histogram_0load:
                out_file_p.write(str(coord)+'\n')

    def run(self):
        self.locateJobs(self.load_config.getLocaterName())
        self.allRoute(self.load_config.getRouteName())
        self.updateAllPortLoad()
        self.getStatistics()

    def testRoute(self):
        """method to test the route algorithm"""
        # coord_src=[0,0,0,0,0,0,0]
        # coord_dst=[7,4,3,2,0,1,1]
        coord_src=[1,2,3,2,1,0,0]
        coord_dst=[5,5,7,2,1,0,0]
        # coord_src=[0, 0, 0, 2, 0, 0, 0]
        # coord_dst=[0, 0, 0, 0, 0, 0, 0]
        # coord_src=[0,0,2,0,0,0,0]
        # coord_dst=[0,0,7,0,0,0,0]
        load=1
        # path=self.routes[0].routing(coord_src,coord_dst,load,self.swports)
        path=self.routes[1].routing(coord_src,coord_dst,load,self.swports)
        # path=self.routes[2].routing(coord_src,coord_dst,load,self.swports)
        for swport in path.swports:
            print(swport.coord)


# topo=Topo([4,4,4,3,2,2],'input\summary.log')
# topo.run()
# topo.locateJobs('QuarterLocater')
# topo.testRoute()
# print(topo.routes[0].name)
# topo.allRoute()
# list1=[1,2,3,4]
# list2=[5,6,7,8,9]
# list1[0:2]=list2[2:4]
# print(list1)

# print(sorted(my_map.keys()))
