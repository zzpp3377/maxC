from topo import Topo
from loadconfig import LoadConfig
import json
import time

# config1={
#     "loadfile":"input/summary.log",
#     "route":{
# 	    "name":"dor",
#         "usedlinks":6
#     },
#     "locater":{
#         "name":"SmallLocaterOneJob",
#         "location":0
#     },
#     "offset":0,
#     "dimensions":{
#         "z":8,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     },
#     "outputpath":""
# }

# config2={
#     "loadfile":"input/summary.log",
#     "route":{
# 	    "name":"dorx",
#         "usedlinks":6
#     },
#     "locater":{
#         "name":"SmallLocaterOneJob",
#         "location":0
#     },
#     "offset":0,
#     "dimensions":{
#         "z":8,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     },
#     "outputpath":""
# }

# config3={
#     "loadfile":"input/summary.log",
#     "route":{
# 	    "name":"dorx",
#         "usedlinks":6
#     },
#     "locater":{
#         "name":"SmallLocaterOneJob",
#         "location":0
#     },
#     "offset":3,
#     "dimensions":{
#         "z":8,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     },
#     "outputpath":""
# }

# loadfile=['input/pattern/1000/summary.log',
#             'input/pattern/cmc_multinode/summary.log',
#             'input/pattern/cns/summary.log',
#             'input/pattern/df_AMG_n1728_dumpi/summary.log',
#             'input/pattern/df_bigfft_n1024_dumpi/summary.log',
#             'input/pattern/FillBoundary_n1000_dumpi/summary.log',
#             'input/pattern/mocfe/summary.log',

#             'input/pattern/multigrid/summary.log',
#             'input/pattern/AMR_MiniApp_n1728_dumpi/summary.log',
#             'input/pattern/lulesh/summary.log',
#             'input/pattern/minife_1152/summary.log',
#             'input/pattern/MultiGrid_C_n1000_dumpi/summary.log',
#             'input/pattern/nekbone/summary.log',
#             'input/pattern/df_bigfft_n1024_med_dumpi/summary.log'
#             ]

# ouputpath=[
#             ['output/pattern/1000/dor/','output/pattern/1000/dorx/','output/pattern/1000/dorx_offset3/'],
#             ['output/pattern/cmc_multinode/dor/','output/pattern/cmc_multinode/dorx/','output/pattern/cmc_multinode/dorx_offset3/'],
#             ['output/pattern/cns/dor/','output/pattern/cns/dorx/','output/pattern/cns/dorx_offset3/'],
#             ['output/pattern/df_AMG_n1728_dumpi/dor/','output/pattern/df_AMG_n1728_dumpi/dorx/','output/pattern/df_AMG_n1728_dumpi/dorx_offset3/'],
#             ['output/pattern/df_bigfft_n1024_dumpi/dor/','output/pattern/df_bigfft_n1024_dumpi/dorx/','output/pattern/df_bigfft_n1024_dumpi/dorx_offset3/'],
#             ['output/pattern/FillBoundary_n1000_dumpi/dor/','output/pattern/FillBoundary_n1000_dumpi/dorx/','output/pattern/FillBoundary_n1000_dumpi/dorx_offset3/'],
#             ['output/pattern/mocfe/dor/','output/pattern/mocfe/dorx/','output/pattern/mocfe/dorx_offset3/'],

#             ['output/pattern/multigrid/dor/','output/pattern/multigrid/dorx/','output/pattern/multigrid/dorx_offset3/'],
#             ['output/pattern/AMR_MiniApp_n1728_dumpi/dor/','output/pattern/AMR_MiniApp_n1728_dumpi/dorx/','output/pattern/AMR_MiniApp_n1728_dumpi/dorx_offset3/'],
#             ['output/pattern/lulesh/dor/','output/pattern/lulesh/dorx/','output/pattern/lulesh/dorx_offset3/'],
#             ['output/pattern/minife_1152/dor/','output/pattern/minife_1152/dorx/','output/pattern/minife_1152/dorx_offset3/'],
#             ['output/pattern/MultiGrid_C_n1000_dumpi/dor/','output/pattern/MultiGrid_C_n1000_dumpi/dorx/','output/pattern/MultiGrid_C_n1000_dumpi/dorx_offset3/'],
#             ['output/pattern/nekbone/dor/','output/pattern/nekbone/dorx/','output/pattern/nekbone/dorx_offset3/'],
#             ['output/pattern/df_bigfft_n1024_med_dumpi/dor/','output/pattern/df_bigfft_n1024_med_dumpi/dorx/','output/pattern/df_bigfft_n1024_med_dumpi/dorx_offset3/']
#         ]

# config=[config1,config2,config3]

# for i in range(0,len(loadfile)):
#     for j in range(0,len(config)):
#         temp_config=config[j]
#         temp_config["loadfile"]=loadfile[i]
#         temp_config["outputpath"]=ouputpath[i][j]
#         # print(temp_config)
#         with open('config/configure.txt','w') as config_file:
#             json.dump(temp_config,config_file)
        
#         print(loadfile[i])

#         time.sleep(5)

#         loadconfig=LoadConfig('config/configure.txt')
#         topo=Topo(loadconfig)
#         topo.run()

####################图11右 start##############################
# temp_config={
#     "loadfile":"input/summary.log",
#     "route":{
# 	    "name":"",
#         "usedlinks":6
#     },
#     "locater":{
#         "name":"",
#         "location":0
#     },
#     "offset":0,
#     "dimensions":{
#         "z":8,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     },
#     "outputpath":""
# }
# locater=["LargeLocaterOneJob","NearLargeLocaterOneJob"]
# route=['dor','dorx']
# dimensions1={
#         "z":8,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     }
# dimensions2={
#         "z":4,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     }
# dimensions3={
#         "z":2,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     }
# dimensions4={
#         "z":2,
#         "y":6,
#         "x":4,
#         "b":3,
#         "c":2,
#         "a":2
#     }
# dimensions=[dimensions1,dimensions2,dimensions3,dimensions4]
# loadfile=['input/8_large/summary.log','input/4_large/summary.log']
# # outputpath=['utput/pattern/multigrid/dor/',]

# for locater_name in locater:
#     temp_config['locater']['name']=locater_name
#     for route_name in route:
#         temp_config['route']['name']=route_name
#         for dimension in dimensions:
#             temp_config['dimensions']=dimension
#             if dimension['x']==8:
#                 temp_config['loadfile']=loadfile[0]
#             else:
#                 temp_config['loadfile']=loadfile[1]
#             outputpath='output/图11右/'+str(locater_name)+"_"+str(dimension['x'])+\
#                     str(dimension['y'])\
#                     +str(dimension['z'])+'_'+str(route_name)+'/'
#             temp_config['outputpath']=outputpath

#             with open('config/configure.txt','w') as config_file:
#                 json.dump(temp_config,config_file)
#             print(outputpath)

#             time.sleep(5)
            
#             loadconfig=LoadConfig('config/configure.txt')
#             topo=Topo(loadconfig)
#             topo.run()
####################图11右 end##############################  

#######################图11左 start#########################
####################图11右 start##############################
# temp_config={
#     "loadfile":"input/summary.log",
#     "route":{
# 	    "name":"",
#         "usedlinks":6
#     },
#     "locater":{
#         "name":"",
#         "location":0
#     },
#     "offset":0,
#     "dimensions":{
#         "z":8,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     },
#     "outputpath":""
# }
# locater=["SmallLocaterOneJob","NearSmallLocaterOneJob"]
# route=['dor','dorx']
# dimensions1={
#         "z":8,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     }
# dimensions2={
#         "z":4,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     }
# dimensions3={
#         "z":2,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     }
# dimensions4={
#         "z":2,
#         "y":6,
#         "x":4,
#         "b":3,
#         "c":2,
#         "a":2
#     }
# dimensions=[dimensions1,dimensions2,dimensions3,dimensions4]
# loadfile=['input/8_small/summary.log','input/4_small/summary.log']
# # outputpath=['utput/pattern/multigrid/dor/',]

# for locater_name in locater:
#     temp_config['locater']['name']=locater_name
#     for route_name in route:
#         temp_config['route']['name']=route_name
#         for dimension in dimensions:
#             temp_config['dimensions']=dimension
#             if dimension['x']==8:
#                 temp_config['loadfile']=loadfile[0]
#             else:
#                 temp_config['loadfile']=loadfile[1]
#             outputpath='output/图11左/'+str(locater_name)+"_"+str(dimension['x'])+\
#                     str(dimension['y'])\
#                     +str(dimension['z'])+'_'+str(route_name)+'/'
#             temp_config['outputpath']=outputpath

#             with open('config/configure.txt','w') as config_file:
#                 json.dump(temp_config,config_file)
#             print(outputpath)

#             time.sleep(5)
            
#             loadconfig=LoadConfig('config/configure.txt')
#             topo=Topo(loadconfig)
#             topo.run()
#######################图11左 end###########################

# ####################图12cd start##############################
# temp_config={
#     "loadfile":"input/summary.log",
#     "route":{
# 	    "name":"",
#         "usedlinks":6
#     },
#     "locater":{
#         "name":"",
#         "location":0
#     },
#     "offset":0,
#     "dimensions":{
#         "z":8,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     },
#     "outputpath":""
# }
# locater=["LargeLocaterOneJob","SmallLocaterOneJob"]
# route=['dor','dorx']
# dimensions1={
#         "z":8,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     }
# dimensions2={
#         "z":4,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     }
# dimensions=[dimensions1,dimensions2]
# offset=[0,1,2,3]
# loadfile=['input/8_large/summary.log','input/8_small/summary.log']
# # outputpath=['utput/pattern/multigrid/dor/',]

# for locater_name in locater:
#     temp_config['locater']['name']=locater_name
#     if locater_name=='LargeLocaterOneJob':
#         temp_config['loadfile']=loadfile[0]
#     else:
#         temp_config['loadfile']=loadfile[1]
#     for dimension in dimensions:
#         temp_config['dimensions']=dimension
#         for route_name in route:
#             temp_config['route']['name']=route_name
            
#             if route_name=='dorx':
#                 for temp_offset in offset:
#                     temp_config['offset']=temp_offset

#                     outputpath='output/图11左/'+str(locater_name)+"_"+str(dimension['x'])+\
#                             str(dimension['y'])\
#                             +str(dimension['z'])+'_'+str(route_name)+"_"+\
#                             "offset"+str(temp_offset)+'/'
#                     temp_config['outputpath']=outputpath

#                     with open('config/configure.txt','w') as config_file:
#                         json.dump(temp_config,config_file)
#                     print(outputpath)

#                     time.sleep(5)
                    
#                     loadconfig=LoadConfig('config/configure.txt')
#                     topo=Topo(loadconfig)
#                     topo.run()
#             else:

#                 outputpath='output/图12cd/'+str(locater_name)+"_"+str(dimension['x'])+\
#                         str(dimension['y'])\
#                         +str(dimension['z'])+'_'+str(route_name)+'/'
#                 temp_config['outputpath']=outputpath

#                 with open('config/configure.txt','w') as config_file:
#                     json.dump(temp_config,config_file)
#                 print(outputpath)

#                 time.sleep(5)
                
#                 loadconfig=LoadConfig('config/configure.txt')
#                 topo=Topo(loadconfig)
#                 topo.run()
# #######################图12cd end###########################

####################图12e start##############################
# temp_config={
#     "loadfile":"input/quarter/summary.log",
#     "route":{
# 	    "name":"",
#         "usedlinks":6
#     },
#     "locater":{
#         "name":"QuarterLocaterOneJob",
#         "location":0
#     },
#     "offset":0,
#     "dimensions":{
#         "z":8,
#         "y":6,
#         "x":8,
#         "b":3,
#         "c":2,
#         "a":2
#     },
#     "outputpath":""
# }
# location=[0,1,2,3]
# route=['dor','dorx']
# offset=[0,1,2,3]
# # outputpath=['utput/pattern/multigrid/dor/',]
# for temp_location in location:
#     temp_config['locater']['location']=temp_location
#     for route_name in route:
#         temp_config['route']['name']=route_name
        
#         if route_name=='dorx':
#             for temp_offset in offset:
#                 temp_config['offset']=temp_offset

#                 outputpath='output/图12e/'+'quarter'+"_"+'location'+str(temp_location)\
#                             +'_868_'+str(route_name)+'offset'+str(temp_offset)+'/'
#                 temp_config['outputpath']=outputpath

#                 with open('config/configure.txt','w') as config_file:
#                     json.dump(temp_config,config_file)
#                 print(outputpath)

#                 time.sleep(5)
                
#                 loadconfig=LoadConfig('config/configure.txt')
#                 topo=Topo(loadconfig)
#                 topo.run()
#         else:

#             outputpath='output/图12e/'+'quarter'+"_"+'location'+str(temp_location)\
#                         +'_868_'+str(route_name)+'/'
#             temp_config['outputpath']=outputpath

#             with open('config/configure.txt','w') as config_file:
#                 json.dump(temp_config,config_file)
#             print(outputpath)

#             time.sleep(5)
            
#             loadconfig=LoadConfig('config/configure.txt')
#             topo=Topo(loadconfig)
#             topo.run()
#######################图12e end###########################

####################图12f start##############################
temp_config={
    "loadfile":"input/half/summary.log",
    "route":{
	    "name":"",
        "usedlinks":6
    },
    "locater":{
        "name":"HalfLocaterOneJob",
        "location":0
    },
    "offset":0,
    "dimensions":{
        "z":8,
        "y":6,
        "x":8,
        "b":3,
        "c":2,
        "a":2
    },
    "outputpath":""
}
location=[0,1,2,3]
route=['dor','dorx']
offset=[0,1,2,3]
# outputpath=['utput/pattern/multigrid/dor/',]
for temp_location in location:
    temp_config['locater']['location']=temp_location
    for route_name in route:
        temp_config['route']['name']=route_name
        
        if route_name=='dorx':
            for temp_offset in offset:
                temp_config['offset']=temp_offset

                outputpath='output/图12f/'+'half'+"_"+'location'+str(temp_location)\
                            +'_868_'+str(route_name)+'offset'+str(temp_offset)+'/'
                temp_config['outputpath']=outputpath

                with open('config/configure.txt','w') as config_file:
                    json.dump(temp_config,config_file)
                print(outputpath)

                time.sleep(5)
                
                loadconfig=LoadConfig('config/configure.txt')
                topo=Topo(loadconfig)
                topo.run()
        else:

            outputpath='output/图12f/'+'half'+"_"+'location'+str(temp_location)\
                            +'_868_'+str(route_name)+'/'
            temp_config['outputpath']=outputpath

            with open('config/configure.txt','w') as config_file:
                json.dump(temp_config,config_file)
            print(outputpath)

            time.sleep(5)
            
            loadconfig=LoadConfig('config/configure.txt')
            topo=Topo(loadconfig)
            topo.run()
#######################图12f end###########################
