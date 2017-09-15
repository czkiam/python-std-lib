#!/usr/bin/env python
"""sample script on using deque - pronounced as DECK"""

from collections import deque
DECK = deque([2,3,4,5,16,17,18,19])

print DECK

print [m for m in dir((list)) if not m.startswith('__')]
print [m for m in dir((deque)) if not m.startswith('__')]

DECK2 = deque(maxlen=5)

DECK2.extend(range(5))
print DECK2

#remove right most item and append item to left
DECK2.append(10)
print DECK2

#remove left most item and append item to right
DECK2.appendleft(0)
print DECK2

primes = [2,3,5,7,11,13,17,19]
prime_deck = deque(primes)
print prime_deck

prime_deck.rotate(4)
print prime_deck

prime_deck.rotate(-2)
print prime_deck

prime_deck.rotate(20)
print prime_deck
