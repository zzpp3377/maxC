from topo import Topo
from loadconfig import LoadConfig
import json
import time

config1={
    "loadfile":"input/summary.log",
    "route":{
	    "name":"dor",
        "usedlinks":6
    },
    "locater":{
        "name":"SmallLocater",
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

config2={
    "loadfile":"input/summary.log",
    "route":{
	    "name":"dorx",
        "usedlinks":6
    },
    "locater":{
        "name":"SmallLocater",
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

config3={
    "loadfile":"input/summary.log",
    "route":{
	    "name":"dorx",
        "usedlinks":6
    },
    "locater":{
        "name":"SmallLocater",
        "location":0
    },
    "offset":3,
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

loadfile=['input/pattern/multigrid/summary.log',
            'input/pattern/AMR_MiniApp_n1728_dumpi/summary.log',
            'input/pattern/lulesh/summary.log',
            'input/pattern/minife_1152/summary.log',
            'input/pattern/MultiGrid_C_n1000_dumpi/summary.log',
            'input/pattern/nekbone/summary.log',
            'input/pattern/df_bigfft_n1024_med_dumpi/summary.log']

ouputpath=[
            ['output/pattern/multigrid/dor/','output/pattern/multigrid/dorx/','output/pattern/multigrid/dorx_offset3/'],
            ['output/pattern/AMR_MiniApp_n1728_dumpi/dor/','output/pattern/AMR_MiniApp_n1728_dumpi/dorx/','output/pattern/AMR_MiniApp_n1728_dumpi/dorx_offset3/'],
            ['output/pattern/lulesh/dor/','output/pattern/lulesh/dorx/','output/pattern/lulesh/dorx_offset3/'],
            ['output/pattern/minife_1152/dor/','output/pattern/minife_1152/dorx/','output/pattern/minife_1152/dorx_offset3/'],
            ['output/pattern/MultiGrid_C_n1000_dumpi/dor/','output/pattern/MultiGrid_C_n1000_dumpi/dorx/','output/pattern/MultiGrid_C_n1000_dumpi/dorx_offset3/'],
            ['output/pattern/nekbone/dor/','output/pattern/nekbone/dorx/','output/pattern/nekbone/dorx_offset3/'],
            ['output/pattern/df_bigfft_n1024_med_dumpi/dor/','output/pattern/df_bigfft_n1024_med_dumpi/dorx/','output/pattern/df_bigfft_n1024_med_dumpi/dorx_offset3/']
        ]

config=[config1,config2,config3]

for i in range(0,len(loadfile)):
    for j in range(0,len(config)):
        temp_config=config[j]
        temp_config["loadfile"]=loadfile[i]
        temp_config["outputpath"]=ouputpath[i][j]
        # print(temp_config)
        with open('config/configure.txt','w') as config_file:
            json.dump(temp_config,config_file)
        
        print(loadfile[i])

        time.sleep(5)

        loadconfig=LoadConfig('config/configure.txt')
        topo=Topo(loadconfig)
        topo.run()


    