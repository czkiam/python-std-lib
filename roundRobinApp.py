from collections import deque
import random

jq = deque()

for j in list('ABCD'):
    jq.append({'label': j, 'completed': random.randint(5, 25)})

while len(jq) > 0:
    current = jq[0]
    current['completed'] -= 5

    if current['completed'] > 0:
        print('job {0} has {1} remaining'.format(current['label'], current['completed']))
    else:
        print('job {0} has completed'.format(current['label']))
        jq.remove(current)

    jq.rotate(1)

print('All job have been completed')

