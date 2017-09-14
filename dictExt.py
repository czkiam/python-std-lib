from collections import defaultdict
from collections import OrderedDict
import random

str_dict = defaultdict(str)

print 'missing key' + str_dict['foo']

float_dict = defaultdict(float)

print float_dict['foo']

int_dict = defaultdict(int)

print int_dict['foo']

int_dict['apples'] += 1

class Fraction(object):
    def __init__(self):
        self.n = 1
        self.d = 2
    def __repr__(self):
        return '{0}/{1}'.format(self.n, self.d)

fraction_dict = defaultdict(Fraction)

print fraction_dict['foo']

def dne(): 
    return 'DNE'

dne_dict = defaultdict(dne)

print dne_dict['foo']

print int_dict
print int_dict['foo']
int_dict['foo'] = 9
print int_dict['foo']


fruits = OrderedDict()

for f in ['apples', 'bananas', 'cherries', 'lemons', 'limes', 'oranges', 'peaches']:
    fruits[f] = random.randint(50, 100)

print fruits

fruits['bananas'] = 50

print fruits

# not avialable in 2.7
#fruits.move_to_end('bananas')

fruits.popitem()
print fruits


fruits.popitem(False)
print fruits

print fruits['apples']
