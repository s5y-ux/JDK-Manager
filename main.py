import os

def artWork():
	with open("ArtWork.txt", "r") as file:
		Lines = file.readlines()
		for line in Lines:
			if(line == Lines[-1]):
				print(line)
			else:
				print(line[0:len(line)-1])

def prompt():
	os.system('clear')
	artWork()
	print("Type \"help\" for a list of commands...")
	promptAnswer = str(input(">: "))
	if(promptAnswer.lower() == "help"):
		helpOutput()
	elif(promptAnswer.lower() == "change"):
		os.system("sudo update-alternatives --config java")
		prompt()
	elif(promptAnswer.lower().split(" ")[0] == "download-jdk"):
		try:
			continueVal = str(input("Download openjdk {}? [Y/n] ".format(promptAnswer.lower().split(" ")[1])))
			if(continueVal.lower() == "y"):
				os.system("sudo apt-get install openjdk-{}-jdk".format(promptAnswer.lower().split(" ")[1]))
				prompt()
		except Exception:
			print()
			print("download-jdk <version> - Downloads the specified jdk")
			returnVal = input()
			prompt()
	elif(promptAnswer.lower() == "exit"):
		assert True
	else:
		helpOutput()
		
def helpOutput():
	print()
	print("help - gets a list of the possible commands.")
	print("change - changes your JDK version")
	print("download-jdk <version> - Downloads the specified jdk")
	print("exit - leave the program")
	returnVal = input()
	prompt()

if __name__ == "__main__":
	artWork()
	print()
	print("Made By: sy5 (Joseph Shumaker)")
	print("Version 1.0.0 (Beta)")
	print("#====================#")
	print()
	prompt()
