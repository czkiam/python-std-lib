#counter extend class sample
from collections import Counter

c = Counter()
c['apples'] += 1
c['bananas'] += 1
c['apples'] += 2
c['cherries'] += 4

print c.most_common() #[('cherries', 4), ('apples', 3), ('bananas', 1)]
print c['lemons']

prose = "Python is so easy to learn and use, that it also might be easy to re-invent the wheel for common tasks. Resist the temptation as the Python Standard Library might have you covered!"
prose = prose.lower()
words = prose.split(' ')
prose_count = Counter()

for word in words:
    prose_count[word[0]] += 1

print prose_count.most_common()
print prose_count.elements()
print prose_count.keys()

fruits = ['apples', 'apples', 'bananas', 'cherries', 'lemons', 'oranges', 'oranges']
shipment = Counter(fruits)

c.update(shipment)
sold = ['apples', 'apples', 'oranges', 'oranges', 'bananas']
c.subtract(sold)

print c.most_common()
