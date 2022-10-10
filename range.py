import time

start = time.time()
my_list = [31, 32, 33]
for x in range(31):
    # print('my lucky number is ' + str(x))
    my_list.append(x)
print(sorted(my_list))
print(eval('5 + 4 *6 +100 /25'))
time.sleep(4)
stop = time.time()
print(stop- start)