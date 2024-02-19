from typing import List

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



class byandsell:
    
    def __init__(self, items):
        self.items = items

    def buy(self, item):
        
        pass

    def sell(self, item):
        
        pass


array_instance = conctenation_of_array(input_array=[0])
unique_array_result = array_instance.getConcatenation()
print(unique_array_result)


