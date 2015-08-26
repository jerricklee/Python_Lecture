def loadDiamond():
	f = open("./diamond", "+r")
	if ( not f ):
		return 0
	print(f.read())

def printDiamond(size):

	loadDiamond()
	if ( size % 2 == 0 ):
		print ("you have to put in odd number")
		return 0
	output = open("diamond", "w")

	halfList = list(range(0, size//2))
	halfList.reverse()
	rowList = list(range(0, size//2+1)) + halfList

	for row in rowList:
		for col in range(0, size//2-row):
			print(" ", end="")
			output.write(" ")
		for col in range(size//2-row, size//2+row+1):
			print("*", end="")
			output.write("*")
		for col in range(size//2+row, size):
			print(" ", end="")
			output.write(" ")
		print("")
		output.write("\n")

def main():
	try:
		size = int(input("put in the size > "))
		printDiamond(size)
	except ValueError:
		print("you have to put in integer")

if __name__ == '__main__':
	main()