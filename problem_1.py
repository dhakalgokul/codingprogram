import functools
import math

# Second configuration: User choice to configure interval in seconds
second_configuration = int(input('Input your second configuration : '))*1000

input_data = [
    "1,10000,40",
    "1,10002,45",
    "1,11015,50",
    "2,10005,42",
    "2,11051,45",
    "2,12064,42",
    "2,13161,42",
]

# create empty list for storing the data from two different sensors
data_list1 = list()
data_list2 = list()

# split the data into two groups Data 1 from Sensor 1 and Data 2 from sensor2
for d in input_data:
    data = list(map(int,d.split(',')))
    if data[0] == 1:
        data_list1.append(data)
    else:
        data_list2.append(data)

# determine the first number and last number for the range
begging_num = (data_list1[0][1]) if data_list1[0][1] <= data_list2[0][1] else data_list2[0][1]

last_num = (data_list1[-1][1]) if data_list1[-1][1] >= data_list2[-1][1] else data_list2[-1][1]
last_num = math.ceil(last_num/1000)*1000

num_config = list(range(begging_num,last_num,second_configuration))

# Initialize the variables data_one and data_two to zero
data_one = 0
data_two = 0

# iterate the whole range
for index in range(len(num_config)):
    temp_list = []

    # list one is the data from sensor1
    # data one is to mark the each point in order not to iterate the same value from the list
    for lone in data_list1[data_one:]:
        time_stamp = lone[1]
        if time_stamp < num_config[index]+999:
            temp_list.append(lone[-1])
            data_one += 1
        else:
            break
    # repeat the same process for the list from sensor2
    for ltwo in data_list2[data_two:]:
        time_stamp = ltwo[1]
        if time_stamp < num_config[index]+999:
            temp_list.append(ltwo[-1])
            data_two += 1
        else:
            break

    # mean value is evaluated each time
    mean = functools.reduce(lambda x, y: x + y, temp_list)/len(temp_list)
    mean = "{:.2f}".format(mean).rstrip('0').rstrip('.')
    print("{}-{}:{}".format(num_config[index], num_config[index] + 999,
                        mean))
