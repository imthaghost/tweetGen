"""
A script that represents the stochastic sampling of a text file

"""
from random import uniform, random
import math

# class dictogram(object):
#     def __init__(self):
#         pass

#     def sum(self):


def sample(histogram, path):
    pass


class Dictogram(object):
    def __init__(self, dictogram):
        self.dictogram = dictogram
        self.sum = sum([self.dictogram.get(key, 0) for key in self.dictogram])

    def get_val(self, key):
        return self.dictogram[key]

    def prob(self, key):
        return self.get_val(key) / self.sum

    def get_random(self):
        #     index = rand.nextInt(totalSum);
        #     int sum = 0;
        #     int i = 0;
        #     while(sum < index) {
        #          sum = sum + items.get(i++).relativeProb;}
        #     return items.get(Math.max(0, i-1));
        # }
        return self.sum * random()


histogram = Dictogram({'fish': 4,
                       'one': 1,
                       'blue': 2,
                       'cat': 3,
                       # 'sum': sum([histogram.get(key, 0) for key in histogram])
                       })
print(histogram.dictogram)
print(histogram.get_val('fish'))
print(histogram.prob('fish'))
print(histogram.get_random())
