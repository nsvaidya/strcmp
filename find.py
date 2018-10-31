# find.py - A small python utility for comparing strings of multiple files located in single folder.
# Created by Neerad Vaidya on 9th Feb, 2018 15:58:15 IST
# Distributed under GNU GPLv3 Licence
import os, timeit,ctypes,sys,datetime
ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,"",None,1)
dat=datetime.datetime.now()
print "Script started @ ",dat
st=timeit.default_timer()
simstri=list()
fl=list()
chkfl=list()
for root, dirs, files in os.walk(os.getcwd()):
	for names in files:
		if names.rfind(".txt") > 0:
			fl+=[names]			
lent=len(fl)
print "File listing & indexing Complete"
for a in range(0,lent):
		for b in range(1,lent):
			if a==b:
				print "Warning!! Delete the duplicate files to avoid confusion"
				continue
			elif (a,b) not in chkfl and (b,a) not in chkfl:
					print "Analyzing File: " + fl[a] + " with " + fl[b]
					filhan1=open(fl[a],"r")
					filhan2=open(fl[b],"r")
					lst1=list()
					lst2=list()
					for line in filhan1:
						lst1+=[line]
					for line in filhan2:
						lst2+=[line]
					filhan1.close()
					filhan2.close()
					if len(lst1) >= len(lst2):
						for items in lst1:
							if items in lst2:
								if items not in simstri:
									print("Match Found")
									simstri+=[items]
								else:
									print("Duplicate Match Found")
									continue
						chkfl+=[(a,b)]
						chkfl+=[(b,a)]
					elif len(lst1) <= len(lst2):
						for items in lst2:
							if items in lst1:
								if items not in simstri:
									print("Match Found")
									simstri+=[items]
								else:
									print("Duplicate Match Found")
									continue
						chkfl+=[(a,b)]
						chkfl+=[(b,a)]
					else:
						print("Unspecified Error")
				else:
					print("Files " + fl[a] + " with " + fl[b] + " are already checked")
fhand=open("result.txt","w")
for items in simstri:
	fhand.write(items)
fhand.close()
stop=timeit.default_timer()
elapsed=stop - st
m, s = divmod(elapsed, 60)
h, m = divmod(m, 60)
print "Script ended @ ", datetime.datetime.now()
print "Total Elapsed Time: %d:%02d:%02d" % (h, m, s)
