import time

def count():
	print('Enter anything to start timer: ')
	input()
	startTime = time.time()
	print('Enter anything to stop timer: ')
	input()
	endTime = time.time()

	timeElapsed = endTime - startTime
	minutes = int(timeElapsed / 60)
	seconds = int(timeElapsed % 60)
	print(str(minutes) +' minute(s) and ' +str(seconds) +' second(s) have passed.')

def setTime():
	print('Enter number of seconds to count down from: ')
	timeStr = input()
	timeInt = int(timeStr)
	while timeInt > 0:
		print(timeInt)
		time.sleep(1)
		timeInt -= 1
	print('Done!')

def main():
	print('Start counting time (1) or set a time to count (2)?: ')
	answer = input()
	if(answer == '1'):
		count()
	elif(answer == '2'):
		setTime()

main()