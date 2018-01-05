
class Locater():
    """this is the class wihch maps process to host"""
    def __init__(self,name):
        self.name=name
    
    def locate(self,dimensions,host,swports,load_module,jobs):
        print('locate method')

class SmallLocater(Locater):
    """this is the class which maps process to host with 'small pattern'"""
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
    def __init__(self,name):
        super().__init__(name)
    
    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        if dimensions[2]%2!=0:
            raise(Exception('the dimension x must be mutiple of 2!!!'))

        hostnum=(dimensions[2]//2)*dimensions[3]*dimensions[4]*dimensions[5] 
        job_index=0           
        for i in range(0,dimensions[0]//2):  #z
            for j in range(0,dimensions[1]):   #y
                #first half
                # print('job :'+str(job_index)+'.1')
                location_x1=0       #location x is the start x coordinate of switch groups
                location_x2=dimensions[2]//2
                
                base_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+index])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+index])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1  

                #second half
                # print('job :'+str(job_index)+'.2')
                location_x1=dimensions[2]//2      #location x is the start x coordinate of switch groups
                location_x2=0
                
                base_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+index])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+index])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1              


class QuarterLocater(Locater):
    """this is the class which maps process to host with 'small pattern'"""
    def __init__(self,name):
        super().__init__(name)
    
    def locate(self,dimensions,hosts,swports,proc_num,jobs):
        """maps process to host with 'small pattern'"""
        if dimensions[2]%4!=0:
            raise(Exception('the dimension x must be mutiple of 4!!!'))

        hostnum=(dimensions[2]//4)*dimensions[3]*dimensions[4]*dimensions[5] 
        job_index=0           
        for i in range(0,dimensions[0]//2):  #z
            for j in range(0,dimensions[1]):   #y
                #first half
                # print('job :'+str(job_index)+'.1')
                location_x1=0       #location x is the start x coordinate of switch groups
                location_x2=dimensions[2]//2
                
                base_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+index])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+index])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1  

                #second half
                # print('job :'+str(job_index)+'.2')
                location_x1=dimensions[2]//4     #location x is the start x coordinate of switch groups
                location_x2=dimensions[2]//2+dimensions[2]//4 
                
                base_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+index])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+index])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1  

                #third half
                # print('job :'+str(job_index)+'.3')
                location_x1=2*dimensions[2]//4     #location x is the start x coordinate of switch groups
                location_x2=0 
                
                base_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+index])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+index])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1   

                #forth half
                # print('job :'+str(job_index)+'.4')
                location_x1=3*dimensions[2]//4     #location x is the start x coordinate of switch groups
                location_x2=dimensions[2]//4 
                
                base_index1=hosts.index(swports[i][j][location_x1][0][0][0][0])
                farthest_i=(i+dimensions[0]//2)%dimensions[0]
                farthest_j=(j+dimensions[1]//2)%dimensions[1]
                base_index2=hosts.index(swports[farthest_i][farthest_j][location_x2][0][0][0][0])
                array=[]
                jobs.append(array)    
                for idx in range(0,proc_num):
                    if idx%(2*hostnum)<hostnum :          # 2 is the magic number for small pattern    
                        index=idx%hostnum  
                        jobs[job_index].append(hosts[base_index1+index])
                    else:
                        index=idx%hostnum
                        jobs[job_index].append(hosts[base_index2+index])
                    # print(jobs[job_index][idx].coord)
                job_index=job_index+1            

class NearSmallLocater(Locater):
    """this is the class which maps process to host with 'near small pattern'"""
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
                print('job :'+str(job_index))          
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
                    print(jobs[job_index][proc_idx].coord)  
                job_index=job_index+1         