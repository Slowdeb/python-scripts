import subprocess, sys, os
from subprocess import Popen
 
with open('random.dic','r',encoding='UTF-8') as f:
#put-the-correct-name
    print("Let's go!")
    for x in f:
        l = str(x).rstrip()
        vl = ["./program",l] #put-the-correct-name
        p = Popen(vl, stdout=subprocess.PIPE).stdout
        q = p.read()
         
        output = (str(q, 'UTF-8'))
        if "Correct" in output:
            os.system('clear')
            print("\n\nFound: ",x,"\nThe msg is:\n\n",output)
            f.close()
            sys.exit()
