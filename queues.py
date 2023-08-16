class Queue:
    def __init__(self,size):
        self.items = []
        self.size = size

    def dequeue_to_enqueue(self):
        if self.is_full:
            print("length of items:",len(self.items))
            print("size of the queue",self.size)
            dequeue_count = len(self.items)-self.size
            return ("The total number of element need to dequeue is",dequeue_count)    

    def is_empty(self):
        return len(self.items)==0

    def is_full(self):
        return len(self.items) == self.size

    def enqueue(self,item):
        if self.is_full():
            print("Queue is Full, try remove the some elements")
        else:
            self.items.append(item)

    # deleting from the front is dequeing
    def dequeue(self):
        if self.is_empty():
            return("Queue is empty")
        else:
            return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return("Queue is empty")
        else:
            return self.items[0]

    def rear(self):
        if self.is_empty():
            return("Queue is empty")
        else:
            return self.items[-1]

    def display(self):
        return self.items



q = Queue(5)
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
print(q.dequeue_to_enqueue())
print(q.display())






class Queue:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.size

    def enqueue(self, item):
        if self.is_full():
            dequeue_count = len(self.items) - self.size + 1
            print(f"You need to dequeue {dequeue_count} times to enqueue one element.")
            return dequeue_count
        else:
            self.items.append(item)
            return 0

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items[0]

    def rear(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.items[-1]

    def display(self):
        return self.items

q = Queue(5)
q.enqueue(1)
q.enqueue(3)
q.enqueue(4)
q.dequeue()
q.enqueue(5)
q.dequeue()
q.enqueue(1)
q.enqueue(4)

print(q.display())




