
####################################
#topo.py
#build a torus topology
####################################
from swport import SwPort
from route import Route,Dor,DorBiu,Dorx
from loadmoudle import LoadMoudle
from path import Path
from locater import SmallLocater,LargeLocater,HalfLocater,QuarterLocater,NearSmallLocater,NearLargeLocater
from locater import SmallLocaterOneJob,LargeLocaterOneJob,HalfLocaterOneJob,QuarterLocaterOneJob,NearSmallLocaterOneJob,NearLargeLocaterOneJob
from locater import AllLocater
from locater import CubeLocater,CubeCLocater
from loadconfig import LoadConfig
from opticalconnectmapper import FarthestMapper

import os

class Topo():
    """the Topo class represent the topology of network"""
    
    def __init__(self,load_config):
        """this dimensions must be a 6 elements list"""
        self.paths=[]
        self.dimensions=load_config.getDimensions()
        self.opticalConnectMap={}
        self.opticalConnectMapper={
            'FarthestMapper':FarthestMapper('FarthestMapper')
        }
        self.routes={
                        'dor':Dor('dor',self.dimensions),
                        'dorbiu':DorBiu('dorbiu',self.dimensions,load_config.getRouteUsedLinks(),load_config.getOpticalWeight(),load_config.getOffset(),self.opticalConnectMap),
                        'dorx':Dorx('dorx',self.dimensions,load_config.getOffset(),self.opticalConnectMap)
                    }
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
                        'NearLargeLocater':NearLargeLocater('NearLargeLocater'),

                        'SmallLocaterOneJob':SmallLocaterOneJob('SmallLocaterOneJob'),
                        'LargeLocaterOneJob':LargeLocaterOneJob('LargeLocaterOneJob'),
                        'HalfLocaterOneJob':HalfLocaterOneJob('HalfLocaterOneJob',load_config.getLocaterLocation()),
                        'QuarterLocaterOneJob':QuarterLocaterOneJob('QuarterLocaterOneJob',load_config.getLocaterLocation()),
                        'NearSmallLocaterOneJob':NearSmallLocaterOneJob('NearSmallLocaterOneJob'),
                        'NearLargeLocaterOneJob':NearLargeLocaterOneJob('NearLargeLocaterOneJob'),
                        
                        'AllLocater':AllLocater('AllLocater'),
                        'CubeLocater':CubeLocater('CubeLocater'),
                        'CubeCLocater':CubeCLocater('CubeCLocater')
                    }
        self.load_config=load_config

        #make topo
        # this represent a 6d-torus
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
                    if load!=0:
                        path=self.routes[route_name].routing(coord_src,coord_dst,load,self.swports)
                        self.paths.append(path)
                    # for swport in path.swports:
                        # print(swport.coord)
    
    def updatePortLoad(self,path):
        """update the load of ports in network"""
        for swport in path.swports:
            # print(str(swport.port_load)+"\t:\t"+str(path.path_load))
            swport.port_load=swport.port_load+path.path_load
    
    def updateAllPortLoad(self):
        """update the load of all ports in network"""
        for path in self.paths:
            self.updatePortLoad(path)
        # for swport in self.line_swports:
            # print('coordinate:'+str(swport.coord)+"\tload:"+str(swport.port_load))

    def getStatistics(self):
        """write statistics to output file"""
        histogram_electric={}
        histogram_optical={}
        histogram_0load=[]
        for swport in self.line_swports:
            if swport.coord[6]!=11 :
                port_load=swport.port_load//1
                if port_load in histogram_electric.keys():
                    histogram_electric[port_load]=histogram_electric[port_load]+1
                else:
                    histogram_electric[port_load]=1 
                # if swport.port_load in histogram_electric.keys():
                #     histogram_electric[swport.port_load]=histogram_electric[swport.port_load]+1
                # else:
                #     histogram_electric[swport.port_load]=1
            else:
                port_load=swport.port_load//1
                if port_load in histogram_optical.keys():
                    histogram_optical[port_load]=histogram_optical[port_load]+1
                else:
                    histogram_optical[port_load]=1
                # if swport.port_load in histogram_optical.keys():
                #     histogram_optical[swport.port_load]=histogram_optical[swport.port_load]+1
                # else:
                #     histogram_optical[swport.port_load]=1
            if swport.port_load==0 :
                histogram_0load.append(swport.coord)
                # print(str(swport.coord))
        
        outputpath=self.load_config.getOutputPath()
        if not os.path.exists(outputpath):
            os.makedirs(outputpath) 
        with open(str(outputpath)+'histogram_electric.txt','w') as out_file_p:
            for key in sorted(histogram_electric.keys()):
                # print(str(key)+"\t"+str(histogram[key]))
                out_file_p.write(str(key)+"\t"+str(histogram_electric[key])+"\n")
        with open(str(outputpath)+'histogram_optical.txt','w') as out_file_p:
            for key in sorted(histogram_optical.keys()):
                out_file_p.write(str(key)+"\t"+str(histogram_optical[key])+"\n")
        with open(str(outputpath)+'histogram_0load.txt','w') as out_file_p:
            for coord in histogram_0load:
                out_file_p.write(str(coord)+'\n')

    def run(self):
        """method to call by main"""
        self.generConnectMap(self.load_config.getOpticalMapperName())
        print('generate connect map success!!!')
        self.locateJobs(self.load_config.getLocaterName())
        print('locate jobs success!!!')
        self.allRoute(self.load_config.getRouteName())
        print("route success!!!")
        self.updateAllPortLoad()
        print("update port load success!!!")
        self.getStatistics()
        print("get statistic success!!!")

    def outLocater(self,outFileName):
        """method to output the locater file"""
        self.locateJobs(self.load_config.getLocaterName())
        with open(outFileName,"w") as outputfp:
            for i in range(0,len(self.jobs)):
                for j in range(0,len(self.jobs[i])):
                    sw=self.jobs[i][j]
                    y_len=self.dimensions[1]
                    x_len=self.dimensions[2]
                    b_len=self.dimensions[3]
                    c_len=self.dimensions[4]
                    a_len=self.dimensions[5]
                    si_len=b_len*c_len*a_len
                    nicIndex=sw.coord[0]*y_len*x_len*si_len+sw.coord[1]*x_len*si_len+sw.coord[2]*si_len+sw.coord[3]*c_len*a_len+sw.coord[4]*a_len+sw.coord[5]
                    outputfp.write(str(nicIndex)+"\t")
                outputfp.write("\n")

    def generConnectMap(self,mapperName):
        """record optical information"""
        self.opticalConnectMapper[mapperName].record(self.dimensions,self.opticalConnectMap)

    def outConnectMap(self,outFileNmae):
        """method to output optical information"""
        with open(outFileNmae,'w') as filep: 
            for i in range(0,self.dimensions[0]):
                for j in range(0,self.dimensions[1]):
                    for k in range(0,self.dimensions[2]):
                        key=(i,j,k)
                        value=self.opticalConnectMap[key]
                        print(str(key)+"<-->"+str(value))
                        filep.write(str(i)+"\t"+str(j)+"\t"+str(k)+"\t"+str(value[0])+"\t"+str(value[1])+"\t"+str(value[2])+"\t"+"\n")

    def testRoute(self):
        """method to test the route algorithm"""
        # coord_src=[0,0,0,0,0,0,0]
        # coord_dst=[7,4,3,2,0,1,1]
        # coord_src=[1,2,3,2,1,0,0]
        # coord_dst=[5,5,7,2,1,0,0]
        # coord_src=[0, 0, 0, 2, 0, 0, 0]
        # coord_dst=[0, 0, 0, 0, 0, 0, 0]
        # coord_src=[0,0,2,0,0,0,0]
        # coord_dst=[0,0,7,0,0,0,0]
        coord_src=[0,0,0,0,0,0,0]
        coord_dst=[4,3,4,0,0,0,0]
        load=1
        # path=self.routes['dor'].routing(coord_src,coord_dst,load,self.swports)
        path=self.routes['dorbiu'].routing(coord_src,coord_dst,load,self.swports)
        # path=self.routes['dorx'].routing(coord_src,coord_dst,load,self.swports)
        for swport in path.swports:
            print(swport.coord)




# loadconfig=LoadConfig('config\configure.txt')
# topo=Topo(loadconfig)
# print("start")
# topo.generConnectMap("FarthestMapper")
# outFileName="output/optical_connect/farthest/connect_map.log"
# topo.outConnectMap(outFileName)

# topo.testRoute()
# for ele in topo.opticalConnectMap.keys():
#     print(str(topo.opticalConnectMap[ele]))

# topo.outLocater("newCube.log")
# topo.run()
# topo.locateJobs('CubeLocater')
# print("end")
# topo.testRoute()
# print(topo.routes[0].name)
# topo.allRoute()
# list1=[1,2,3,4]
# list2=[5,6,7,8,9]
# list1[0:2]=list2[2:4]
# print(list1)

# print(sorted(my_map.keys()))

