############################
#locater.py 
#locate algorithm
############################
import pdb

class Locater():
    """this is the class wihch maps process to host"""
    def __init__(self,name):
        self.name=name
    
    def locate(self,dimensions,host,swports,load_module,jobs):
        print('locate method')

class SmallLocater(Locater):
    """this is the class which maps process to host with 'small pattern'"""
    """将应用部署在两组X维度上连续且Y、Z维度上欧拉距离最远的硅元"""
    def __init__(self,name):
        super().__init__(name)
    
    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0            
        for i in range(0,dimensions[0]//2):  #z
            for j in range(0,dimensions[1]):   #y
                # load_moudle=LoadMoudle(filename)  
                base_index1=hosts.index(swports[i][j][0][0][0][0][0])
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
                array=[]
                jobs.append(array)    
                # print('job:'+str(job_index))
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+index])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+index])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1              

class LargeLocater(Locater):
    """this is the class which maps process to host with 'large pattern'"""
    """将应用部署在X维度上连续，Y、Z维度上最远的四组硅元上.应用所占的终端个数是SmallLocater的2倍，可以看作是两个SmallLocater所部署的应用的组合"""
    def __init__(self,name):
        super().__init__(name)

    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]  
        job_index=0          
        for i in range(0,dimensions[0]//2):  #z
            for j in range(0,dimensions[1]//2):   #y
                base_index1=hosts.index(swports[i][j][0][0][0][0][0])
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
                base_index3=hosts.index(swports[i][farthest_j][0][0][0][0][0])
                base_index4=hosts.index(swports[farthest_i][j][0][0][0][0][0])
                array=[]
                # print('job :'+str(job_index))          
                jobs.append(array)    
                for proc_idx in range(0,proc_num):              
                    if proc_idx%(4*hostnum)<hostnum :          # 4 is the magic number for small pattern    
                        index=proc_idx%hostnum                 #index is the switch offset index about base switch in host list   
                        jobs[job_index].append(hosts[base_index1+index])
                    elif proc_idx%(4*hostnum)<2*hostnum:
                        index=proc_idx%hostnum
                        jobs[job_index].append(hosts[base_index2+index])
                    elif proc_idx%(4*hostnum)<3*hostnum:
                        index=proc_idx%hostnum
                        jobs[job_index].append(hosts[base_index3+index])
                    else:
                        index=proc_idx%hostnum
                        jobs[job_index].append(hosts[base_index4+index])
                    # print(jobs[job_index][proc_idx].coord)  
                job_index=job_index+1            

class HalfLocater(Locater):
    """this is the class which maps process to host with 'small pattern'"""
    """将应用部署在X维度上连续且长度只有X维度一半的，Y、Z维度上最远的两组硅元上。应用所占的终端个数是SmallLocater的一半，可以看作是半个SmallLocater所部署的应用。"""
    def __init__(self,name,location):
        super().__init__(name)
        self.location=location

    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        if dimensions[2]%2!=0:
            raise(Exception('the dimension x must be mutiple of 2!!!'))
        if self.location>dimensions[2]//2:
            raise(Exception('the location must less or equal than half the length of dimension x!!!'))

        hostnum=(dimensions[2]//2)*dimensions[3]*dimensions[4]*dimensions[5]
        x_dimension_hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0           
        for i in range(0,dimensions[0]//2):  #z
            for j in range(0,dimensions[1]):   #y
                #first half
                # print('job :'+str(job_index)+'.1')
                location_x1=0       #location x is the start x coordinate of switch groups
                location_x2=dimensions[2]//2-self.location
                
                base_index1=hosts.index(swports[i][j][0][0][0][0][0])
                offset_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])-base_index1
                
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
                offset_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])-base_index2
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum:          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+(index+offset_index1)%x_dimension_hostnum])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+(index+offset_index2)%x_dimension_hostnum])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1  

                #second half
                # print('job :'+str(job_index)+'.2')
                location_x1=dimensions[2]//2      #location x is the start x coordinate of switch groups
                location_x2=(0+dimensions[2]-self.location)%dimensions[2]
                
                base_index1=hosts.index(swports[i][j][0][0][0][0][0])
                offset_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])-base_index2
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
                offset_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])-base_index2
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+(index+offset_index1)%x_dimension_hostnum])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+(index+offset_index2)%x_dimension_hostnum])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1              

class QuarterLocater(Locater):
    """this is the class which maps process to host with 'small pattern'"""
    """将应用部署在X维度上连续且长度只有X维度四分之一的，Y、Z维度上最远的两组硅元上。应用所占的终端个数是SmallLocater的四分之一，可以看作是四分之一个SmallLocater所部署的应用。"""
    def __init__(self,name,location):
        super().__init__(name)
        self.location=location

    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        if dimensions[2]%4!=0:
            raise(Exception('the dimension x must be mutiple of 4!!!'))
        if self.location>dimensions[2]//2:
            raise(Exception('the location must less or equal than half the length of dimension x!!!'))

        hostnum=(dimensions[2]//4)*dimensions[3]*dimensions[4]*dimensions[5] 
        x_dimension_hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0           
        for i in range(0,dimensions[0]//2):  #z
            for j in range(0,dimensions[1]):   #y
                #first half
                # print('job :'+str(job_index)+'.1')
                location_x1=0       #location x is the start x coordinate of switch groups
                location_x2=dimensions[2]//2-self.location
                
                base_index1=hosts.index(swports[i][j][0][0][0][0][0])
                offset_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])-base_index1
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
                offset_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])-base_index2
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+(index+offset_index1)%x_dimension_hostnum])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+(index+offset_index2)%x_dimension_hostnum])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1  

                #second half
                # print('job :'+str(job_index)+'.2')
                location_x1=dimensions[2]//4     #location x is the start x coordinate of switch groups
                location_x2=dimensions[2]//2+dimensions[2]//4-self.location 
                
                base_index1=hosts.index(swports[i][j][0][0][0][0][0])
                offset_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])-base_index1
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
                offset_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])-base_index2
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+(index+offset_index1)%x_dimension_hostnum])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+(index+offset_index2)%x_dimension_hostnum])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1  

                #third half
                # print('job :'+str(job_index)+'.3')
                location_x1=2*dimensions[2]//4     #location x is the start x coordinate of switch groups
                location_x2=(0+dimensions[2]-self.location)%dimensions[2] 
                
                base_index1=hosts.index(swports[i][j][0][0][0][0][0])
                offset_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])-base_index1
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
                offset_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])-base_index2
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+(index+offset_index1)%x_dimension_hostnum])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+(index+offset_index2)%x_dimension_hostnum])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1   

                #forth half
                # print('job :'+str(job_index)+'.4')
                location_x1=3*dimensions[2]//4     #location x is the start x coordinate of switch groups
                location_x2=(dimensions[2]//4+dimensions[2]-self.location)%dimensions[2] 
                
                base_index1=hosts.index(swports[i][j][0][0][0][0][0])
                offset_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])-base_index1
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
                offset_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])-base_index2
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+(index+offset_index1)%x_dimension_hostnum])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+(index+offset_index2)%x_dimension_hostnum])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1            

class NearSmallLocater(Locater):
    """this is the class which maps process to host with 'near small pattern'"""
    """应用分布在两组X维度上连续，Y、Z维度上距离为1的硅元上。应用所占的终端个数与SmallLocater相同。"""
    def __init__(self,name):
        super().__init__(name)
    
    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0            
        for i in range(0,dimensions[0],2):  #z
            for j in range(0,dimensions[1]):   #y
                # load_moudle=LoadMoudle(filename)  
                base_index1=hosts.index(swports[i][j][0][0][0][0][0])
                near_i=(i+1)%dimensions[0]
                near_j=(j+1)%dimensions[1]
                base_index2=hosts.index(swports[near_i][near_j][0][0][0][0][0])
                array=[]
                jobs.append(array)    
                # print('job:'+str(job_index))
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+index])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+index])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1       

class NearLargeLocater(Locater):
    """this is the class which maps process to host with 'large pattern'"""
    """应用分布在四组X维度上连续，Y、Z维度上距离为1的硅元上。应用所占的终端个数与LargeLocater相同。"""
    def __init__(self,name):
        super().__init__(name)

    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]  
        job_index=0          
        for i in range(0,dimensions[0],2):  #z
            for j in range(0,dimensions[1],2):   #y
                base_index1=hosts.index(swports[i][j][0][0][0][0][0])
                near_i=(i+1)%dimensions[0]
                near_j=(j+1)%dimensions[1]
                base_index2=hosts.index(swports[near_i][near_j][0][0][0][0][0])
                base_index3=hosts.index(swports[i][near_j][0][0][0][0][0])
                base_index4=hosts.index(swports[near_i][j][0][0][0][0][0])
                array=[]
                # print('job :'+str(job_index))          
                jobs.append(array)    
                for proc_idx in range(0,proc_num):              
                    if proc_idx%(4*hostnum)<hostnum :          # 4 is the magic number for small pattern    
                        index=proc_idx%hostnum                 #index is the switch offset index about base switch in host list   
                        jobs[job_index].append(hosts[base_index1+index])
                    elif proc_idx%(4*hostnum)<2*hostnum:
                        index=proc_idx%hostnum
                        jobs[job_index].append(hosts[base_index2+index])
                    elif proc_idx%(4*hostnum)<3*hostnum:
                        index=proc_idx%hostnum
                        jobs[job_index].append(hosts[base_index3+index])
                    else:
                        index=proc_idx%hostnum
                        jobs[job_index].append(hosts[base_index4+index])
                    # print(jobs[job_index][proc_idx].coord)  
                job_index=job_index+1 


########################one job start########################
class SmallLocaterOneJob(Locater):
    """this is the class which maps process to host with 'small pattern'"""
    """网络中只有一个应用，该应用部署在两组X维度上连续且Y、Z维度上欧拉距离最远的硅元上"""
    def __init__(self,name):
        super().__init__(name)
    
    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0            
        i=0
        j=0

        base_index1=hosts.index(swports[i][j][0][0][0][0][0])
        farthest_i=(i+dimensions[0]//2)%dimensions[0]
        farthest_j=(j+dimensions[1]//2)%dimensions[1]
        base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
        array=[]
        jobs.append(array)    
        # print('job:'+str(job_index))
        for idx in range(0,proc_num):
            if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                index=idx%hostnum  
                jobs[job_index].append(hosts[base_index1+index])
            else:
                index=idx%hostnum
                jobs[job_index].append(hosts[base_index2+index])
            # print(jobs[job_index][idx].coord)
        job_index=job_index+1              

class LargeLocaterOneJob(Locater):
    """this is the class which maps process to host with 'large pattern'"""
    """网络中只有一个应用，该应用部署在将应用部署在X维度上连续，Y、Z维度上最远的四组硅元上.应用所占的终端个数是SmallLocaterOneJob的2倍，可以看作是两个SmallLocaterOneJob所部署的应用的组合"""
    def __init__(self,name):
        super().__init__(name)

    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]  
        job_index=0     
        i=0
        j=0     

        base_index1=hosts.index(swports[i][j][0][0][0][0][0])
        farthest_i=(i+dimensions[0]//2)%dimensions[0]
        farthest_j=(j+dimensions[1]//2)%dimensions[1]
        base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
        base_index3=hosts.index(swports[i][farthest_j][0][0][0][0][0])
        base_index4=hosts.index(swports[farthest_i][j][0][0][0][0][0])
        array=[]
        # print('job :'+str(job_index))          
        jobs.append(array)    
        for proc_idx in range(0,proc_num):              
            if proc_idx%(4*hostnum)<hostnum :          # 4 is the magic number for small pattern    
                index=proc_idx%hostnum                 #index is the switch offset index about base switch in host list   
                jobs[job_index].append(hosts[base_index1+index])
            elif proc_idx%(4*hostnum)<2*hostnum:
                index=proc_idx%hostnum
                jobs[job_index].append(hosts[base_index2+index])
            elif proc_idx%(4*hostnum)<3*hostnum:
                index=proc_idx%hostnum
                jobs[job_index].append(hosts[base_index3+index])
            else:
                index=proc_idx%hostnum
                jobs[job_index].append(hosts[base_index4+index])
            # print(jobs[job_index][proc_idx].coord)  
        job_index=job_index+1            

class HalfLocaterOneJob(Locater):
    """this is the class which maps process to host with 'small pattern'"""
    """网络中只有一个应用，该应用部署在X维度上连续且长度只有X维度一半的，Y、Z维度上最远的两组硅元上。应用所占的终端个数是SmallLocaterOneJob的一半，可以看作是半个SmallLocaterOneJob所部署的应用。"""
    def __init__(self,name,location):
        super().__init__(name)
        self.location=location

    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        if dimensions[2]%2!=0:
            raise(Exception('the dimension x must be mutiple of 2!!!'))
        if self.location>dimensions[2]//2:
            raise(Exception('the location must less or equal than half the length of dimension x!!!'))

        hostnum=(dimensions[2]//2)*dimensions[3]*dimensions[4]*dimensions[5]
        x_dimension_hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0 
        i=0
        j=0          

        location_x1=0       #location x is the start x coordinate of switch groups
        location_x2=dimensions[2]//2-self.location
        
        base_index1=hosts.index(swports[i][j][0][0][0][0][0])
        offset_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])-base_index1
        
        farthest_i=(i+dimensions[0]//2)%dimensions[0]
        farthest_j=(j+dimensions[1]//2)%dimensions[1]
        base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
        offset_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])-base_index2
        array=[]
        jobs.append(array)    
        for idx in range(0,proc_num):
            if idx%(2*hostnum)<hostnum:          # 2 is the magic number for small pattern    
                index=idx%hostnum  
                jobs[job_index].append(hosts[base_index1+(index+offset_index1)%x_dimension_hostnum])
            else:
                index=idx%hostnum
                jobs[job_index].append(hosts[base_index2+(index+offset_index2)%x_dimension_hostnum])
            # print(jobs[job_index][idx].coord)
        job_index=job_index+1             

class QuarterLocaterOneJob(Locater):
    """this is the class which maps process to host with 'small pattern'"""
    """网络中只有一个应用，该应用部署在X维度上连续且长度只有X维度四分之一的，Y、Z维度上最远的两组硅元上。应用所占的终端个数是SmallLocaterOneJob的四分之一，可以看作是四分之一个SmallLocaterOneJob所部署的应用。"""
    def __init__(self,name,location):
        super().__init__(name)
        self.location=location

    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        if dimensions[2]%4!=0:
            raise(Exception('the dimension x must be mutiple of 4!!!'))
        if self.location>dimensions[2]//2:
            raise(Exception('the location must less or equal than half the length of dimension x!!!'))

        hostnum=(dimensions[2]//4)*dimensions[3]*dimensions[4]*dimensions[5] 
        x_dimension_hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0  
        i=0
        j=0         

        location_x1=0       #location x is the start x coordinate of switch groups
        location_x2=dimensions[2]//2-self.location
        
        base_index1=hosts.index(swports[i][j][0][0][0][0][0])
        offset_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])-base_index1
        farthest_i=(i+dimensions[0]//2)%dimensions[0]
        farthest_j=(j+dimensions[1]//2)%dimensions[1]
        base_index2=hosts.index(swports[farthest_i][farthest_j][0][0][0][0][0])
        offset_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])-base_index2
        array=[]
        jobs.append(array)    
        for idx in range(0,proc_num):
            if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                index=idx%hostnum  
                jobs[job_index].append(hosts[base_index1+(index+offset_index1)%x_dimension_hostnum])
            else:
                index=idx%hostnum
                jobs[job_index].append(hosts[base_index2+(index+offset_index2)%x_dimension_hostnum])
            # print(jobs[job_index][idx].coord)
        job_index=job_index+1           

class NearSmallLocaterOneJob(Locater):
    """this is the class which maps process to host with 'near small pattern'"""
    """网络中只有一个应用，该应用分布在两组X维度上连续，Y、Z维度上距离为1的硅元上。应用所占的终端个数与SmallLocaterOneJob相同。"""
    def __init__(self,name):
        super().__init__(name)
    
    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0
        i=0
        j=0            

        base_index1=hosts.index(swports[i][j][0][0][0][0][0])
        near_i=(i+1)%dimensions[0]
        near_j=(j+1)%dimensions[1]
        base_index2=hosts.index(swports[near_i][near_j][0][0][0][0][0])
        array=[]
        jobs.append(array)    
        # print('job:'+str(job_index))
        for idx in range(0,proc_num):
            if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                index=idx%hostnum  
                jobs[job_index].append(hosts[base_index1+index])
            else:
                index=idx%hostnum
                jobs[job_index].append(hosts[base_index2+index])
            # print(jobs[job_index][idx].coord)
        job_index=job_index+1       

class NearLargeLocaterOneJob(Locater):
    """this is the class which maps process to host with 'large pattern'"""
    """网络中只有一个应用，该应用分布在四组X维度上连续，Y、Z维度上距离为1的硅元上。应用所占的终端个数与LargeLocaterOneJob相同。"""
    def __init__(self,name):
        super().__init__(name)

    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]  
        job_index=0 
        i=0
        j=0         

        base_index1=hosts.index(swports[i][j][0][0][0][0][0])
        near_i=(i+1)%dimensions[0]
        near_j=(j+1)%dimensions[1]
        base_index2=hosts.index(swports[near_i][near_j][0][0][0][0][0])
        base_index3=hosts.index(swports[i][near_j][0][0][0][0][0])
        base_index4=hosts.index(swports[near_i][j][0][0][0][0][0])
        array=[]
        # print('job :'+str(job_index))          
        jobs.append(array)    
        for proc_idx in range(0,proc_num):              
            if proc_idx%(4*hostnum)<hostnum :          # 4 is the magic number for small pattern    
                index=proc_idx%hostnum                 #index is the switch offset index about base switch in host list   
                jobs[job_index].append(hosts[base_index1+index])
            elif proc_idx%(4*hostnum)<2*hostnum:
                index=proc_idx%hostnum
                jobs[job_index].append(hosts[base_index2+index])
            elif proc_idx%(4*hostnum)<3*hostnum:
                index=proc_idx%hostnum
                jobs[job_index].append(hosts[base_index3+index])
            else:
                index=proc_idx%hostnum
                jobs[job_index].append(hosts[base_index4+index])
            # print(jobs[job_index][proc_idx].coord)  
        job_index=job_index+1     
########################one job end########################


#########################all start###########################
class AllLocater(Locater):
    """this is the class which maps process to host with 'all in one job'"""
    """将应用部署在整个网络中"""
    def __init__(self,name):
        super().__init__(name)
    
    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        hostnum=dimensions[0]*dimensions[1]*dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0            
        base_index=hosts.index(swports[0][0][0][0][0][0][0])  
        array=[]
        jobs.append(array)    
        # print('job:'+str(job_index))
        for idx in range(0,proc_num):
            index=idx%hostnum
            jobs[job_index].append(hosts[base_index+index])
            # print(jobs[job_index][idx].coord)
#########################all stop###########################
#########################cube start###########################
class CubeLocater(Locater):
    """this is the class which maps process to host with 'cube pattern'"""
    """将应用部署在两个相距最远的长度为2的立方体上"""
    def __init__(self,name):
        super().__init__(name)
    
    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0            
        for job_z in range(0,dimensions[0]//2,2):  #z
            for job_y in range(0,dimensions[1],2):   #y
                for job_x in range(0,dimensions[2],2): #x
                    host_in_this_job=[]
                    for z in range(job_z,job_z+2):
                        for y in range(job_y,job_y+2):
                            for x in range(job_x,job_x+2):
                                for b in range(0,3):
                                    for c in range(0,2):
                                        for a in range(0,2):
                                            # pdb.set_trace()
                                            host_in_this_job.append(swports[z%dimensions[0]][y%dimensions[1]][x%dimensions[2]][b%dimensions[3]][c%dimensions[4]][a%dimensions[5]][0])
                    farthest_job_z=(job_z+dimensions[0]//2)%dimensions[0]
                    farthest_job_y=(job_y+dimensions[1]//2)%dimensions[1]
                    farthest_job_x=(job_x+dimensions[2]//2)%dimensions[2]
                    for z in range(farthest_job_z,farthest_job_z+2):
                        for y in range(farthest_job_y,farthest_job_y+2):
                            for x in range(farthest_job_x,farthest_job_x+2):
                                for b in range(0,3):
                                    for c in range(0,2):
                                        for a in range(0,2):
                                            host_in_this_job.append(swports[z%dimensions[0]][y%dimensions[1]][x%dimensions[2]][b%dimensions[3]][c%dimensions[4]][a%dimensions[5]][0])
                    this_job=[]
                    # print('job:'+str(job_index))
                    for idx in range(0,proc_num):
                        this_job.append(host_in_this_job[idx%len(host_in_this_job)])
                    jobs.append(this_job)

                    # for idx in range(0,proc_num):
                    #     print(jobs[job_index][idx].coord)

                    job_index=job_index+1 
#########################cube stop###########################     
#########################CubeC start###########################
class CubeCLocater(Locater):
    """this is the class which maps process to host with 'cube C pattern'"""
    """将应用部署在两个相距最远的长度为2的立方体上,且为C型部署"""
    def __init__(self,name):
        super().__init__(name)
    
    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        # hostnum=dimensions[2]*dimensions[3]*dimensions[4]*dimensions[5]
        job_index=0            
        for job_z in range(0,dimensions[0]//2,2):  #z
            for job_y in range(0,dimensions[1],2):   #y
                for job_x in range(0,dimensions[2],2): #x
                    host_in_this_job=[]
                    for z in range(job_z,job_z+2):
                        for y in range(job_y,job_y+2):
                            for x in range(job_x,job_x+2):
                                for b in range(0,3):
                                    for c in range(0,2):
                                        for a in range(0,2):
                                            # pdb.set_trace()
                                            host_in_this_job.append(swports[z%dimensions[0]][y%dimensions[1]][x%dimensions[2]][b%dimensions[3]][c%dimensions[4]][a%dimensions[5]][0])
                    farthest_job_z=(job_z+dimensions[0]//2)%dimensions[0]
                    farthest_job_y=(job_y+dimensions[1]//2)%dimensions[1]
                    farthest_job_x=(job_x+dimensions[2]//2)%dimensions[2]
                    for z in range(farthest_job_z,farthest_job_z+2):
                        for y in range(farthest_job_y,farthest_job_y+2):
                            for x in range(farthest_job_x,farthest_job_x+2):
                                for b in range(0,3):
                                    for c in range(0,2):
                                        for a in range(0,2):
                                            host_in_this_job.append(swports[z%dimensions[0]][y%dimensions[1]][x%dimensions[2]][b%dimensions[3]][c%dimensions[4]][a%dimensions[5]][0])
                    this_job=[]
                    # print('job:'+str(job_index))
                    for idx in range(0,proc_num):
                        if (idx//len(host_in_this_job))%2 == 0:
                            this_job.append(host_in_this_job[idx%len(host_in_this_job)])
                        else:
                            this_job.append(host_in_this_job[len(host_in_this_job)-1-idx%len(host_in_this_job)])
                    
                    jobs.append(this_job)

                    # for idx in range(0,proc_num):
                    #     print(jobs[job_index][idx].coord)

                    job_index=job_index+1 
#########################cube stop###########################   





