import time

print('Enter anything to start timer: ')
input()
startTime = time.time()
print('Enter anything to stop timer: ')
input()
endTime = time.time()
print(endTime - startTime)
