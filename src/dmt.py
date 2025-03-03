from Debug_module import Debug_module
import time

dm = Debug_module()

print("message 1:")
message = input()
mode = input()
i = 2

while message != "start":
	print(f"message {i}")
	dm.errorMessage(message, mode)
	message = input()
	mode = input()
	i += 1
	
start = time.time()
end = 15
enlapsedTime = 0

print("test start")
while enlapsedTime < end:
	dm.screenRefresh()
	enlapsedTime = time.time() - start
	
	
print("done.")
