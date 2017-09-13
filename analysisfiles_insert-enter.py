##use idle, input one by one: insert '\n' before '}' in the files to a new files
import os
#check current dir, or change dir to the aim dir
os.listdir()
os.chdir('D:\python_analysis_homecss')
#check file exists
if not os.path.exists('home.css'):
    exit(-1)
lines = open('home.txt').readlines()
infile = open('home2.txt', 'w')
for s in lines:
    infile.write(s.replace('}', '}\n')


infile.close()
