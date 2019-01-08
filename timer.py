import time

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

