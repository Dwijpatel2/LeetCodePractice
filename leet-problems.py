from typing import List

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
        
        print(self.input_array)
        return t


     
     

        

class byandsell:
    
    def __init__(self, items):
        self.items = items

    def buy(self, item):
        
        pass

    def sell(self, item):
        
        pass


array_instance = remove_elements(input_array=[0,0,1,1,1,2,2,3,3,4], val=3)
unique_array_result = array_instance.removeElement()
print(unique_array_result)


