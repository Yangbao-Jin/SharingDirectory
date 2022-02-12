from random import *
import numpy as np

class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self) :
        if len(self.data) == 0:
            return True
        return False

    def push(self, value) :
        self.data.append(value)

    def pop(self) :
        if not self.is_empty():
            return self.data.pop()
        return

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        return


class Queue:
    def __init__(self):
        self.data = []


    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def enqueue(self, value):
        self.data.insert(0, value)

    def dequeue(self) :
        return self.data.pop()

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        return

if __name__ == '__main__':

    deck = []
    x = 0

    repeat_four_times = [1, 2, 3, 4]
    for i in repeat_four_times:
        for value in range(1, 14):
            deck.append(value)
            x += 1

    shuffle(deck)

    y = np.array_split(deck, 3)
    p1_cards = y[0]
    p2_cards = y[1]
    p3_cards = y[2]

    P1Queue = Queue()
    P2Queue = Queue()
    P3Queue = Queue()
    TableStack = Stack()

    for i in p1_cards:
        P1Queue.enqueue(i)

    for i in p2_cards:
        P2Queue.enqueue(i)

    for i in p3_cards:
        P3Queue.enqueue(i)

    hand1 = P1Queue.data
    hand2 = P2Queue.data
    hand3 = P3Queue.data

    for item1 in hand1:
        deck.remove(item1)
    for item2 in hand2:
        deck.remove(item2)
    for item3 in deck:
        TableStack.push(item3)

    print(f"Player 1's deck: {P1Queue.data}")
    print(f"Player 2's deck: {P2Queue.data}")
    print(f"Player 3's deck: {P3Queue.data}")

    while True:

        while P1Queue.peek()==TableStack.peek():
            P1Queue.enqueue(TableStack.pop())

        P1Queue.dequeue()
        if P1Queue.is_empty()==True:
            print("Play1 win!")
            break

        while P2Queue.peek() == TableStack.peek():
            P2Queue.enqueue(TableStack.pop())

        P2Queue.dequeue()
        if P2Queue.is_empty() == True:
            print("Play2 win!")
            break

        while P3Queue.peek() == TableStack.peek():
            P3Queue.enqueue(TableStack.pop())

        P3Queue.dequeue()
        if P3Queue.is_empty() == True:
            print("Play3 win!")
            break