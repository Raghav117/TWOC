MAX = 100005
fibonacci = set() 
   


def createHash(): 
  
    global fibonacci 
      
    
    
    prev , curr = 0, 1
    fibonacci.add(prev) 
    fibonacci.add(curr) 
   
    
    
    while (curr <= MAX): 
        temp = curr + prev 
        if temp <= MAX: 
            fibonacci.add(temp) 
        prev = curr 
        curr = temp 
   


def checkArray(arr, n): 
  
    
    
    sum = 0
      
    
    for i in range( n ): 
        if (arr[i] in fibonacci): 
            sum += arr[i] 
   
    
    
    if (sum in fibonacci): 
        return True
   
    return False
   

if __name__ == "__main__": 
      
        
    lst = [] 
    
    n = int(input("Enter number of elements : ")) 

    for i in range(0, n): 
        ele = int(input()) 
    
        lst.append(ele)
   
    
    
    createHash() 
   
    if (checkArray(lst, n)): 
        print("Yes") 
    else: 
        print("No") 