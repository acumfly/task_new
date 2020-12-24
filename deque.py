class Element():

    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 

class Deque:
    counter=0

    def __init__(self):
        self.head = None
        self.tail=None


    def push_tail(self, value):
        Deque.counter+=1
        if self.tail is None:
            self.head = Element(value)
            self.tail =self.head
        else:
            self.tail.next = Element(value)
            self.tail.next.prev=self.tail
            self.tail = self.tail.next
    
    def push_head(self, value):
        Deque.counter+=1
        if self.head is None:
            self.tail = Element(value)
            self.head = self.tail
        else:
            self.head.next=Element(value)
            self.head.next.prev=self.head
            self.head = self.head.next


    def pop_head(self):
        Deque.counter=Deque.counter-1
        if self.head is None:
            return None
        else:
            sv= self.head.value
            self.head = self.head.next
            self.head.prev=None
            return sv
    
    def pop_tail(self):
        Deque.counter=Deque.counter-1
        if self.tail is None:
            return None
        else:
            sv=self.tail.value
            self.tail=self.tail.prev
            self.tail.next=None
            return sv
            
   
    def size(self):
        return(Deque.counter)
    
    def clear(self):
        self.head=None
        self.tail=None
        Deque.counter=0
        print("The deque is clear, check 'size()' method")

   
e = Deque()
e.push_tail("Hello")
e.push_tail(5)
e.push_tail([1, 2, 3, 4])
e.push_tail(1)


print("There is/are", e.size(), "elements in total.")

print(e.pop_head(), "is deleted")
print(e.pop_tail(), "is deleted")
print(e.pop_tail(), "is deleted")

print("There is/are", e.size(), "elements in total.")
e.clear()
print("There is/are", e.size(), "elements in total.")
