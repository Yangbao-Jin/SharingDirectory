from random import *

deck = []
x = 0

p1_deck = []
p2_deck = []
repeat_four_times = [1, 2, 3, 4]
for i in repeat_four_times:
    for value in range(1, 14):
        deck.append(value)
        x += 1

shuffle(deck)


class P1Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def enqueue(self, value):
        self.data.insert(0, value)

    def dequeue(self):
        return self.data.pop()

    def remove(self, index):
        return self.data.pop(index)

    def peek(self, index):
        if not self.is_empty():
            return self.data[index]
        return

    def index(self, element):
        return self.data.index(element)

    def length(self):
        return len(self.data)

    def print_queue(self):
        return self.data

class P2Queue:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def enqueue(self, value):
        self.data.insert(0, value)

    def dequeue(self):
        return self.data.pop()

    def remove(self, index):
        return self.data.pop(index)

    def peek(self, index):
        if not self.is_empty():
            return self.data[index]
        return

    def index(self, element):
        return self.data.index(element)

    def length(self):
        return len(self.data)

    def print_queue(self):
        return self.data

y = 0
for l in deck:
    if y < 26:
        queue = P1Queue()
        queue.enqueue(l)
    else:
        queue = P2Queue()
        queue.enqueue(l)

    y += 1

class TableDeckQueue:
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

    def remove(self, index):
        return self.data.pop(index)

    def peek(self, index):
        if not self.is_empty():
            return self.data[index]
        return

    def index(self, element):
        return self.data.index(element)

    def length(self):
        return len(self.data)

x = 0
while P1Queue.is_empty == False and P2Queue.is_empty == False:
    table_deck_queue = TableDeckQueue()

    if x % 2 == 0: # if p1 deck

        for i in table_deck_queue:
            if i == P1Queue.peek(0):
                index = table_deck_queue.index(i)
                length = table_deck_queue.length()
                s = index-length
                k = 1
                while k != length-index + 2:
                    P1Queue.enqueue(table_deck_queue.peek(-1))
                    table_deck_queue.dequeue()
                    k += 1
                break

            else:
                table_deck_queue.enqueue(P1Queue.index(0))
                P1Queue.remove(0)


    else: # P2's turn
        for i in table_deck_queue:
            if i == P2Queue.peek[0]:
                index = table_deck_queue.index(i)
                length = table_deck_queue.length()
                s = index-length
                k = 1
                while k != length-index + 2:
                    P2Queue.enqueue(table_deck_queue.peek())
                    table_deck_queue.dequeue()
                    k += 1
                break

            else:
                table_deck_queue.enqueue(P2Queue.index(0))
                P2Queue.remove(0)

else:
    if P1Queue.is_empty == True:
        print("Player 1 will win this game!")

    else:
        print("Player 2 will win this game!")

p1_queue = P1Queue()
p2_queue = P2Queue()
print(f"Player 1's deck: {p1_queue.data}")
print(f"Player 2's deck: {p2_queue.data}")
