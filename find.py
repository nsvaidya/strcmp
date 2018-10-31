# find.py - A small python utility for comparing strings of multiple files located in single folder.
# Created by Neerad Vaidya on 9th Feb, 2018 15:58:15 IST
# Distributed under GNU GPLv3 Licence


import os, timeit,ctypes,sys,datetime


ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,"",None,1)

print "Script started @ ",datetime.datetime.now()

# timer initialisation 
st=timeit.default_timer()

# defining lists
simstri=list()
fl=list()
chkfl=list()

# parsing files in the current working directory and appending it to fl list 
for root, dirs, files in os.walk(os.getcwd()):
	for names in files:
		if names.rfind(".txt") > 0:
      # grabbing fl list length 
			fl+=[names]
lent=len(fl)
print "File listing & indexing Complete"


for a in range(0,lent-1):
		#starting a+1 to avoid regoing through same files with different combo b,a / a,b 
		for b in range(a+1,lent):
			if a==b:
				print "Warning!! Delete the duplicate files to avoid confusion"
				continue
			elif (a,b) not in chkfl and (b,a) not in chkfl:
					print "Analyzing File: " + fl[a] + " with " + fl[b]
					# opening files in read mode
					filhan1=open(fl[a],"r")
					filhan2=open(fl[b],"r")
					# defining new lists to contain lines of each file
					lst1=list()
					lst2=list()
					# filling content of the file withing declared lists
					for line in filhan1:
						lst1+=[line]
					for line in filhan2:
						lst2+=[line]
					filhan1.close()
					filhan2.close()

					# checking which file containts more lines and parsing
					if len(lst1) >= len(lst2):
						# parsing the first list for possible match
						for items in lst1:
							if items in lst2:
								if items not in simstri:
									print("Match Found")
									simstri+=[items]
								else:
									print("Duplicate Match Found")
									continue
						# appending file combo to checked file list
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
          # creating result.txt file with matches from simstri list
					print("Files " + fl[a] + " with " + fl[b] + " are already checked")
fhand=open("result.txt","w")
for items in simstri:
	fhand.write(items)
#closing file
fhand.close()
# calculating elapsed time for the algo 
stop=timeit.default_timer()
elapsed=stop - st
m, s = divmod(elapsed, 60)
h, m = divmod(m, 60)

print "Script ended @ ", datetime.datetime.now()
print "Total Elapsed Time: %d:%02d:%02d" % (h, m, s)
 
