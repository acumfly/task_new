class Element():

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    counter = 0

    def __init__(self):
        self.head = None
        self.tail = None

    def push_tail(self, value):
        self.counter += 1
        if self.tail is None:
            self.head = Element(value)
            self.tail = self.head
        else:
            self.tail.next = Element(value)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def push_head(self, value):
        self.counter += 1
        if self.head is None:
            self.tail = Element(value)
            self.head = self.tail
        else:
            self.head.next = Element(value)
            self.head.next.prev = self.head
            self.head = self.head.next

    def pop_head(self):
        if self.head is None:
            return None
        else:
            self.counter-=1
            sv = self.head.value
            self.head = self.head.next
            return sv

    def pop_tail(self):
        if self.tail is None:
            return None
        else:
            self.counter-=1
            sv = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            return sv

    def size(self):
        return(self.counter)

    def clear(self):
        self.head = None
        self.tail = None
        self.counter = 0
        print("The deque is clear, check 'size()' method")
