from Error_manager import Error_manager

em = Error_manager()

em.fileAppend("this is a test message")

message = input()

while message != "exit":
	em.fileAppend(message)
	message = input()
print("done")
