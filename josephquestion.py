class Node:
   def __init__(self, dataval=None):
      self.data = dataval
      self.next = None

class RLinkedList:
   def __init__(self):
      self.head=None

   def removednode(self,number):
      pointer=self.head

      if pointer !=None:
         while(pointer.data !=number):
            prev=pointer
            pointer=pointer.next


         prev.next=pointer.next
         return pointer
      else:

         return

if __name__=='__main__':

   # Create unidirectional rotatiing linked list

   m=9
   n=30
   p=[]
   deadlist=[]
   circle=RLinkedList()
   p.append(Node(1))

   circle.head=p[0]

   for i in range(1,n):
      p.append(Node(i+1))
      p[i-1].next=p[i]
   p.append(Node(n))
   p[n-1].next=p[0]

   # pickup the persons who call m

   pleft=n/2
   premovedNo=0
   i=1
   person = circle.head

   while premovedNo<n/2:

      while i!=m:

         person=person.next
         i = i + 1
      i=1
      circle.removednode(person.data)
      deadlist.append(person.data)
      person=person.next
      premovedNo += 1

   deadlist.sort()
   print deadlist












