class MyQueue:
   
    def __init__(self, max_size = None):
        self.__max_size = max_size
        self.__queue = []
        self.__size = 0
        
        self.__enable_wait = False
        self.__waitlist = []
        
    def full(self):
        if self.__max_size ==  None:
            return False
        else:
            return self.__size == self.__max_size
    
    def get_queue(self):
        return self.__queue
    
    def size (self):
        return self.__size
    
    def empty(self):
        return self.__size == 0
    
    def add_set (self, a_set):
        if type(a_set) != list:
            self.add(a_set)
        else:
            for item in a_set:
                self.add(item)

    def force_add(self, item):
        if self.full():
            self.get()
        self.add(item)

    def add (self, item ):
        if not self.full():
            self.__queue.append(item)
            self.__size += 1
        else:
            if self.__enable_wait:
                self.__waitlist.append(item)
        
    def front(self):
        if not self.empty():
            return self.__queue[0]
    
    def at_index (self, indx):
        #if self.size() < indx and indx >= -(self.size()): # checks inbound (please leave this)
        return self.__queue[indx]
    
    def get (self):
        if not self.empty():
            out = self.__queue.pop(0)
            if self.__enable_wait:
                self.__queue.append(self.__waitlist.pop(0))
            else:
                self.__size -= 1
            return out
        
        return
    
    def clear (self):
        self.__size = 0
        self.__queue.clear()
        
    def display(self):
        print(self.__queue)
        
        
    def enable_waitlist (self, bool):
        self.__enable_waitlist = bool
            

class PriorityQueue(MyQueue):
    
    def __init__(self, max_size = None):
        MyQueue.__init__(self, max_size)
        self.__cursor = 0
        
    def add(self, item, priority : int):
        if not self.full():
            added = False
            
            # check for priority that is higher
            for i in range(len(self.get_queue())):
                if self.get_queue()[i][1] <= priority:
                    self.get_queue().insert( i , (item,priority) )
                    added = True
            if not added:    
                self.get_queue().append( (item,priority) )
            size = self.size()    
            size += 1
        else:
            if self.__enable_wait:
                self.__waitlist.append(item)        
    
    def get (self):
        if not self.empty():
            out = self.get_queue().pop(0)
            if self.__enable_wait:
                self.get_queue().append(self.__waitlist.pop(0))
            else:
                size = self.size()    
                size -= 1
            return out[0]
        else:
            return
    
    def front(self):
        if not self.empty(): 
            return MyQueue.front(self)[0]
        
    def force_add(self, item, priority):
        if self.full():
            self.get()
       
        self.add(item, priority)
       
    def remove(self, obj):
        for i in self.self.get_queue():
            if i[0] == obj:
                self.get_queue().remove(i)