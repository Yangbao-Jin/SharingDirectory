class Node:
   def __init__(self, dataval=None):
      self.data = dataval
      self.next = None

class RLinkedList:
   def __init__(self):
      self.head=None
      self.currentposition=0

   def listprint(self):
      printval = self.head
      while printval is not None:
         print(printval.data)
         printval = printval.next

   def traverse(self):
      self.x = self.head
      while self.x is not None:
         return self.x.data

      self.x = self.x.next

   def length(self, node):
      count = 0
      while node:
         count += 1
         node = node.next
      return count


   def removednode(self,number):
      pointer=self.head
      if pointer !=None:
         while(pointer.data !=number):
            prev=pointer
            nextnode=pointer.next
            pointer=nextnode

         prev.next=pointer.next
         return pointer
      else:
         return


if __name__=='__main__':

   # Create unidirectional rotatiing linked list

   m=9
   n=30
   p=[]
   circle=RLinkedList()
   p.append(Node(1))

   circle.head=p[0]


   for i in range(1,n):
      p.append(Node(i+1))
      p[i-1].next=p[i]
   p.append(Node(n))
   p[n-1].next=p[0]

   s = []

   for i in range(0,30):
      s.append(p[i].data)

   # pickup the persons who call m
   while True:
      while range(0, 8):
         circle.traverse()

         if len(circle) == m/2:
            break

      else:
         circle.traverse()
         circle.removednode(circle.x)
         if len(circle) == m/2:
            break

   # for k in range(0, 15):
   #    print(p[k].data)




