import math
import functools


class SensorDataset():

    def __init__(self, config=None, data=None):
        # Data initialization
        # second manipulation
        self.second_configuration = config
        if type(self.second_configuration) is not int or self.second_configuration is None:
            """ config is set to Default"""
            self.second_configuration = 1000

        self.data = data
        if self.data is None:
            """ Set data to Default"""
            self.data = [
                "1,10000,40",
                "1,10002,45",
                "1,11015,50",
                "2,10005,42",
                "2,11051,45",
                "2,12064,42",
                "2,13161,42",
            ]
        self.data_list1 = list()
        self.data_list2 = list()
        self.data_mean = {}
        self.dataArrange()
        self.set_mean_dict()

    def dataArrange(self):
        # split the data into two groups Data 1 from Sensor 1/ Data 2 from sensor2
        for d in self.data:
            t_data = list(map(int, d.split(',')))
            self.data_list1.append(t_data) if t_data[0] == 1 else self.data_list2.append(t_data)

    def set_mean_dict(self):
        # determine the first number and last number for the range
        begging_num = (self.data_list1[0][1]) if self.data_list1[0][1] <= self.data_list2[0][1] else self.data_list2[0][
            1]
        last_num = (self.data_list1[-1][1]) if self.data_list1[-1][1] >= self.data_list2[-1][1] else \
        self.data_list2[-1][1]

        last_num = math.ceil(last_num / 1000) * 1000

        num_config = list(range(begging_num, last_num, self.second_configuration))
        data_one = 0
        data_two = 0

        for num in num_config:
            temp_list = []
            l_range = num+self.second_configuration

            # list one is the data from sensor1
            # data one is to mark the each point in order not to iterate the same value from the list
            # slicing memoization
            for lone in self.data_list1[data_one:]:
                time_stamp = lone[1]
                if time_stamp < l_range:
                    temp_list.append(lone[-1])
                    data_one += 1
                else:
                    break

            # repeat the same process for the list from sensor2
            for ltwo in self.data_list2[data_two:]:
                time_stamp = ltwo[1]
                if time_stamp < l_range:
                    temp_list.append(ltwo[-1])
                    data_two += 1
                else:
                    break

            # In case of the error when list is empty
            try:
                mean = functools.reduce(lambda x, y: x + y, temp_list) / len(temp_list)
            except TypeError as e:
                mean = 0
            finally:
                mean_key = str(num)+"-" + str(l_range-1)
                self.data_mean[mean_key] = mean


    def get_mean_dict(self):
        for k,v in self.data_mean.items():
            # round the number from .2 point
            # delete all 0 after decimal point
            v = "{:.2f}".format(float(v)).rstrip('0').rstrip('.')
            print("{}:{}".format(k, v))
        return self.data_mean

my_sensor = SensorDataset(config=1000)
print(my_sensor.get_mean_dict())