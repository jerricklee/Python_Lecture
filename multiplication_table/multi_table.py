def makeList(endNum):
	xList = list(range(1, endNum//3+1))
	for x in xList:
		xList[x-1] = xList[x-1] * 3 - 1
	return xList

def multi_table(endNum):
	xList = makeList(endNum)
	for x in xList:
		for y in range(1, 10):
			if ( x <= endNum ):
				print(x, "*", y, "=", x*y, end="\t")
			if ( x+1 <= endNum ):
				print(x+1, "*", y, "=", (x+1)*y, end="\t")
			if ( x+2 <= endNum ):
				print(x+2, "*", y, "=", (x+2)*y)
			else:
				print("")
		print("")

def main():
	try:
		endNum = int(input("put in the last number > "))
		multi_table(endNum)
	except:
		print("you have to put in integer")

if __name__ == '__main__':
	main()