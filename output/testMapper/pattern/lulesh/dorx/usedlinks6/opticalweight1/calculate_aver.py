import re 
filename=['histogram_electric.txt','histogram_optical.txt']
column_1_list=[]
column_2_list=[]
multi_list=[]

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

# print(aver)
# print(max_port_num)
# list=[]
# list.    