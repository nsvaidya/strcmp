# find.py - A small python utility for comparing strings of multiple files located in single folder.
# Created by Neerad Vaidya on 9th Feb, 2018 15:58:15 IST
# Distributed under GNU GPLv3 Licence
import os, timeit,ctypes,sys,datetime,time
ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,"",None,1)
dat=datetime.datetime.now()
print "Script started @ ",dat
st=timeit.default_timer()
simstri=set()
fl=list()
chkfl=list()
for root, dirs, files in os.walk(os.getcwd()):
	for names in files:
		if names.rfind(".txt") > 0:
			fl.append(names)			
lent=len(fl)
print "File listing & indexing Complete"
starttime=time.time()
for a in range(0,lent):
	for b in range(1,lent):
		if a==b:
			print "Same File, Can't Compare"
			continue
		else:
			if (a,b) not in chkfl and (b,a) not in chkfl:
				print "Analyzing File: " + fl[a] + " with " + fl[b]
				filhan1=open(fl[a],"r")
				filhan2=open(fl[b],"r")
				#lst1=list()
				#lst2=list()
				hm1 = set()
				for line in filhan1:
					hm1.add(line)
				for line in filhan2:
					#lst2.append(line)
					if line in hm1:
						print "Match Found"
						simstri.add(line)
					
				chkfl.append((a,b))
				chkfl.append((b,a))
				filhan1.close()
				filhan2.close()
			else:
				print "Files " + fl[a] + " with " + fl[b] + " are already checked"
fhand=open("result.txt","w")
print(str((time.time()-starttime)*1000))
for items in simstri:
	fhand.write(items)
fhand.close()
stop=timeit.default_timer()
elapsed=stop - st
m, s = divmod(elapsed, 60)
h, m = divmod(m, 60)
print "Script ended @ ", datetime.datetime.now()
print "Total Elapsed Time: %d:%02d:%02d" % (h, m, s)
