from Deck import *
from Hand import *
from Card import *


A = Card('2', "Heart")
B = Deck()
P1 = Hand()
P2 = Hand()
B.Deal([P1, P2])

print(A)
print(B)
print(P1)
print(P2)

