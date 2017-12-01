import os

def listFileToTxt(dir,file,wildcard,recursion):
    exts=wildcard.split(" ")
    files=os.listdir(dir)

    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname)&(not name.startswith("."))):
            print("dir======")
            if(os.listdir(fullname)):
                file.write("  "*recursion+name+"\n")
                listFileToTxt(fullname,file,wildcard,recursion+1)
        else:
            for ext in exts:
                nameno = os.path.splitext(name)[1]
                if((nameno==ext)&(not name.startswith("~"))):
                    file.write("  "*recursion+name+"\n")
                    break


def Test():
    dir="//cnnjsdoc//folds//04. Competence"
	#dir=os.getcwd()
    out="out.txt"
    wildcard=".pptx .ppt .docx .doc .pdf .pptm"

    file=open(out,"w")
    if not file:
        print("cannot open the file %s for writting" % out)

    listFileToTxt(dir,file,wildcard,1)
    
    file.close()

if __name__=='__main__':
    Test()
