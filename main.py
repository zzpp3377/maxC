from topo import Topo
from loadconfig import LoadConfig

loadconfig=LoadConfig('config/configure.txt')
topo=Topo(loadconfig)
# topo.locateJobs('NearLargeLocaterOneJob')
topo.run()