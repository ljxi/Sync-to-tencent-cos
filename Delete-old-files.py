import subprocess,os
cmd=lambda x:subprocess.Popen(x, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8').communicate()[0]
Cos_str=cmd('coscmd list -ar -n 100000 /')
Cos_list=[i.split("   ")[1] for i in Cos_str.split("\n")[:-1]]
Local_list=[]
for path,dir_list,file_list in os.walk("./"):  
    path=path.split("./")[1]
    for file_name in file_list:  
        Local_list.append("%s%s%s"%(path,'/' if path else '',file_name))
to_delete=[]
for i in Cos_list:
    if i not in Local_list:
        to_delete.append(i)
for i in to_delete:
    print('Delete: %s'%i)
    cmd('coscmd delete -f %s'%i)
print("Delete old files done!")
