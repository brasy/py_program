import os
import string

def anaRecords(dir,file,diffile):
    resultlist=[]
    f_records=open(dir,"r")
    lines=f_records.readlines()
    for line in lines:
        if line not in resultlist:
            resultlist.append(line)
            file.write(line)
        elif ((line in resultlist)&(line.find(".")>0)):
            diffile.write(line)
    f_records.close()
	    
def Test():
    dir="out.txt"
    out="out_ana.txt"
    difout="out_dif.txt"

    file=open(out,"w")
    if not file:
        print("cannot open the file %s for writting" % out)
    diffile=open(difout,"w")

    anaRecords(dir,file,diffile)

    file.close()
    diffile.close()

if __name__=='__main__':
    Test()
