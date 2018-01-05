这是一个网络负载分析程序：
语言：python3
环境：python3.5.3
      Visual studio code 1.19.1

该程序主要思想：
	当一个网络拓扑已知，路由算法已知，应用的通信模式与部署方式已知的时候，
可以直接计算出网络中每个端口（链路）的负载。

各个模块介绍：
	loadmoudle：主要包含LoadMoudle类，负责从load文件中读取应用的负载信息
	locater：主要包含Locater、SmallLocater类，负责部署应用到网络中的节点上，
		Locator是父类，SmallLocater是一种部署方式的具体实现。若使用其他
		部署方式，需要继承Locator，并对其locate方法进行覆写。
	path：主要包含Path类，记录通信路径，包含路径所经过的端口，路径的负载等信息。
	route：主要包含Route、Dor、Dorbiu、Dorx类，路由算法类，主要包含维序路由算法，
		以及两种新路由算法（参考专利《一种面向链路资源的自适应互连与路由控制
		方法和系统》、。。。。）。若要使用新路由算法，需要继承Route类，并对其
		routing方法进行覆写。
	swport：主要包含SwPort类，端口类，代表交换机的端口。
	topo：主要包含Topo类，代表拓扑，这里主要实现了一个6d-torus拓扑。
	main：程序入口
路径:
	input:负载文件存放路径，loadmoudle模块从该路径summary.log文件读取应用的通信负载
	output：程序输出存放位置，这里程序统计了不同负载的端口数目，并输出到该路径下的文件中。

