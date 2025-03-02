from Print_manager import Print_manager
import time
import random

pm = Print_manager()

# static
val = [0, 0, 0, 0, 0]

#dinamic
dval = ["string1", "string2", "string3", "string4", "string5"]
pm.setDinamicQueue(dval)

i = 0
start = time.time()

dvalt = [start, start, start, start, start]
pm.setScreenTimeQueue(dvalt)

end = 5
enlapsedTime = 0
while enlapsedTime < end:
	
	pm.refresh()
	
	i = 0
	for v in val:
		v = random.randint(1, 100)
		val[i] = v
		i += 1
		
	pm.setStaticQueue(val)
	
	enlapsedTime = time.time() - start

pm.dPrintAppend("append1")
pm.dPrintAppend(f"{pm.getDinamicQueue()}")
pm.sPrintAppend(101)	
end = 2
enlapsedTime = 0
start = time.time()
while enlapsedTime < end:
	
	pm.refresh()
	
	i = 0
	for v in val:
		v = random.randint(1, 100)
		val[i] = v
		i += 1
		
	pm.setStaticQueue(val)
	
	enlapsedTime = time.time() - start
	
end = 7
pm.dPrintAppend("append2")
enlapsedTime = 0
start = time.time()
while enlapsedTime < end:
	
	pm.refresh()
	
	i = 0
	for v in val:
		v = random.randint(1, 100)
		val[i] = v
		i += 1
		
	pm.setStaticQueue(val)
	
	enlapsedTime = time.time() - start

print("done")
