
proc_num=192
with open("cubeAlltoall.log","w") as output_file:
    for src in range(0,proc_num):
        for dst in range(0,proc_num):
            if src!=dst:
                output_file.write("1\t")
            else:
                output_file.write("0\t")    
        output_file.write("\n")    