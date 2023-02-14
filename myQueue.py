class MyQueue:
   
    def __init__(self, max_size = None):
        self.__max_size = max_size
        self.__queue = []
        self.__size = 0
     
        
    def is_full(self):
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
        if self.is_full():
            self.get()
        self.add(item)

    def add (self, item ):
        if not self.is_full():
            self.__queue.append(item)
            self.__size += 1
        
    def front(self):
        if not self.empty():
            return self.__queue[0]
    
    def at_index (self, indx):
        #if self.size() < indx and indx >= -(self.size()): # checks inbound (please leave this)
        return self.__queue[indx]
    
    def get (self):
        if not self.empty():
            out = self.__queue.pop(0)
            self.__size -= 1
            return out
        return
    def push(self, item):
         """
         Adds item to the queue pushing the front item if the queue is full 
         """
         if self.is_full():
            self.get()
         self.add(item)
    def clear (self):
        self.__size = 0
        self.__queue.clear()
        
    def display(self):
        print(self.__queue)
        

class PriorityQueue(MyQueue):
    """
    A queue in which automatically sorts objects in queue by given priority from highest priority 
    being at the front of the queue and the lowest at the end of the queue, respectively 
    """
    def __init__(self, max_size = None):
        MyQueue.__init__(self, max_size)
        self.__cursor = 0
        
    def add(self, item, priority : int):
        if not self.is_full():
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
              
    def force_add(self, item, priority):
         """
         Will force add item into the queue, if queue is full at time of execution, the lowest priority item will be removed from queue
         """
         
         if self.is_full():
            lowest_priority_object = self.get_queue()[-1] 
            self.remove(lowest_priority_object)

         self.add(item, priority)
    def push(self, item, priority):
         if self.is_full():
            self.get()
         self.add(item, priority)
    def remove(self, item):
         """
         Removes a given item from the queue
         
         WARNING:
         - if the queue has copies of the item with different priority, the wrong itme could be removed
         """
         for item_and_priority in self.self.get_queue():
            if item_and_priority[0] == item:
                self.get_queue().remove(item_and_priortiy)
                  
                  
