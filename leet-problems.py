from typing import List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# problem 26
class remove_duplicate_from_array: 
     def __init__(self, input_array):
        self.input_array = input_array
        

     def RemoveDuplicateFromArray(self) -> List[int]:
        
        i = 1
        t = 1
        while i < len(self.input_array):
            if self.input_array[i] != self.input_array[i-1]:
                self.input_array[t] = self.input_array[i]
                t += 1    
            i += 1
        return t

# problem 27          
class remove_elements: 

    def __init__(self, input_array, val):
        self.input_array = input_array
        self.val = val

    def removeElement(self) -> List[int]:
        
        i = 0
        t = 0
        while i < len(self.input_array):
            if self.input_array[i] != self.val:
                self.input_array[t] = self.input_array[i]
                t += 1    
            i += 1
       
        return t


# problem 1929
class conctenation_of_array:
    
    def __init__(self, input_array) -> None:
        self.input_array = input_array

    def getConcatenation(self):
        
        length = len(self.input_array)
        array = []
        t = 0
        i = 0

        while i < length * 2:
            array.append(self.input_array[t])
            t += 1
           
            if t == length:
                t = 0
            
            i += 1
            
        return array


# problem 682   
class baseball_game:

    def __init__(self, input_array) -> None:
        self.input_array = input_array
    
    def calPoints(self): 
        
        i = 0 
        t = 0 
        num1 = 0
        num2 = 0
        stack = []
        
        while i < len(self.input_array):
            

            if self.input_array[i] == '+':
                num3 = num1 
                num1 = num2
                num2 = num1 + num3
                stack.append(num2)
                t =  num2 + t
                
               
            elif self.input_array[i] == 'D':
                
                num1 = num2 
                num2 = num2 * 2
                stack.append(num2)
                t = num2 + t
              
            elif self.input_array[i] == 'C':
                if stack:
                    num3 = stack.pop()
                    if stack:
                        num2 = stack.pop()
                        if stack:
                            num1 = stack.pop()
                            stack.append(num1)
                        else: 
                            num1 = 0    
                        stack.append(num2)
                    else:
                        num2 = num1                   
                    t = t - num3
            else: 
                num3 = int(self.input_array[i])
                stack.append(num3)
                num1 = num2
                num2 = num3
                t = num2 + t 
                
            i += 1    

        return t
    




# problem 206
class reverse_linked_list: 
    def __init__(self, values=None):
        if values is None:
            values = []

        if values:
            self.head = ListNode(values[0])
            current = self.head
            for val in values[1:]:
                current.next = ListNode(val)
                current = current.next
        else:
            self.head = None
    
    def reverseList(self):
        new_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = new_head
            new_head = current
            current = next_node
        
        return new_head 



#problem 707
class my_linked_list: 

    def __init__(self):
        self.size = 0
        self.head = None

    def get(self, index: int) -> int:
        if index < 0 or index > self.size: 
            return -1
        prev = self.head 

        for _ in range(index):
            prev = prev.next 
        return prev.next.val 

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index >= self.size: 
            return
        
        prev = self.head

        self.size += 1 
        for _ in range(index):
            prev = prev.next

        add_to = ListNode(val)

        add_to.next = prev.next
        prev.next = add_to



    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size: 
            return
        
        prev = self.head

        self.size -= 1 
        for _ in range(index):
            prev = prev.next

        prev.next = prev.next.next


#problem 876    
class middle_of_the_linked_list: 
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def middleNode(self):
        current = self.head
        queue = []
        while current:
            queue.append(current.val)
            current = current.next
            
        size = len(queue)/2
        
        if not isinstance(size, int):
            size = len(queue) - int(size  + 0.5) 
        
        print(size)
        print(queue)

        queue = queue[size:]
        print(queue)
        return queue
        

 

class byandsell:
    
    def __init__(self, items):
        self.items = items

    def buy(self, item):
        
        pass

    def sell(self, item):
        
        pass


linked_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5,ListNode(6))))))
array_instance = middle_of_the_linked_list(linked_list)
test = array_instance.middleNode()

print(test)



