import os
f=open("Recorder.xlsx")
(fpath,fname)=os.path.split(f.name)
os.path.splitext(fname)
