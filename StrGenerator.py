import os
import json
import sys
import datetime
import random
import string

N = sys.argv[1]
#print(datetime.datetime.now().strftime("%H:%M:%S"))
fl = open(datetime.datetime.now().strftime("%H%M%S")+".txt", "w")

for a in range(100000):
  fl.write(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(int(N))) + "\n")
  
fl.close()