from Debug_module import Debug_module
from Communication_module import Communication_module
import time

def stop(start, end):
	if time.time() - start > end:
		return True
	else:
		return False

def main(args):
	dm = Debug_module()
	cm = Communication_module()
	cm.setDebugger(dm)
	

	cm.serverInit("cmt3")
	
	cm.respondServer("(move -10 10)", False)
	playerResponse = "(turn 150)"
	
	
	end = 15
	print(f"wait {end} secconds.")
	start = time.time()
	while not stop(start, end):
		cm.listenServer()
		cm.respondServer(playerResponse, True)
		#print(message)
		
	cm.respondServer("(bye)", False)
		
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
