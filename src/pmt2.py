from Print_manager import Print_manager
import time
import random

pm = Print_manager()

# static
# val = [0, 0, 0, 0, 0]

val = [["name1", 0], ["name2", 0], ["name3", 0], ["name4", 0], ["name5", 0]]

#dinamic

dval = ["dstring1", "dstring2", "dstring3"]

for v in dval:
	pm.dPrintAppend(v)

i = 0
start = time.time()

dvalt = [start, start, start, start, start]
pm.setScreenTimeQueue(dvalt)

pm.setStaticQueue(val)

end = 5
enlapsedTime = 0
while enlapsedTime < end:
	
	pm.refresh()
	
	i = 0
	for v in val:
		v[1] = random.randint(1, 100)
		i += 1	

	enlapsedTime = time.time() - start

pm.dPrintAppend("dappend1")

sValue = ["sValue", 101]
pm.sPrintAppend(sValue)
	
end = 2
enlapsedTime = 0
start = time.time()
while enlapsedTime < end:
	
	pm.refresh()
	
	i = 0
	for v in val:
		v[1] = random.randint(1, 100)
		i += 1	

	enlapsedTime = time.time() - start
	
end = 7
pm.dPrintAppend("dappend2")

enlapsedTime = 0
start = time.time()
while enlapsedTime < end:
	
	pm.refresh()
	
	i = 0
	for v in val:
		v[1] = random.randint(1, 100)
		i += 1	

	enlapsedTime = time.time() - start

pm.sRemove("name2")

end = 7
enlapsedTime = 0
start = time.time()
while enlapsedTime < end:
	
	pm.refresh()
	
	i = 0
	for v in val:
		v[1] = random.randint(1, 100)
		i += 1	

	enlapsedTime = time.time() - start


print("done")
