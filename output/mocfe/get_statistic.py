import re 
import os
filename=['histogram_electric.txt','histogram_optical.txt']
column_1_list=[]
column_2_list=[]
multi_list=[]


def run_once():
    for i in range(0,2):
        with open(filename[i]) as filep:
            linelist=filep.readlines()
            for line in linelist:
                line=re.split('\t|\n',line)
                line.pop(-1)
                column_1_list.append(float(line[0]))
                column_2_list.append(float(line[1]))
                multi_list.append(column_1_list[-1]*column_2_list[-1])
                # print(str(multi_list[-1]))

    column_2_sum=0.0
    for temp in column_2_list:
        column_2_sum=temp+column_2_sum
    
    multi_sum=0.0
    for temp in multi_list:
        multi_sum=multi_sum+temp

    aver=multi_sum/column_2_sum
    column_2_list.sort()
    max_column_2=column_2_list[-1]
    column_1_list.sort()
    max_column_1=column_1_list[-1]
    with open("statistic.txt",'w') as outputfp:
        outputfp.write("average:"+str(aver)+'\n')
        outputfp.write("column 2 max:"+str(max_column_2)+'\n')
        outputfp.write("column 1 max:"+str(max_column_1)+'\n')
        
    column_2_list.clear()
    column_1_list.clear()
    multi_list.clear()

dirlist=os.listdir()
dirlist.remove("get_statistic.py")
# dirlist.remove("未完成.txt")
# print(dirlist)
now_path=os.getcwd()
print(now_path)
for dir in dirlist:
    os.chdir(dir)
    dirlist2=os.listdir()
    now_path2=os.getcwd()
    for dir2 in dirlist2:
        os.chdir(dir2)
        dirlist3=os.listdir()
        now_path3=os.getcwd()
        for dir3 in dirlist3:
            os.chdir(dir3)
            dirlist4=os.listdir()
            now_path4=os.getcwd()
            for dir4 in dirlist4:
                os.chdir(dir4)
                run_once()
                os.chdir(now_path4)
            os.chdir(now_path3)
        os.chdir(now_path2)
    os.chdir(now_path)

# print(aver)
# print(max_port_num)
# list=[]
# list.re    