list_values = [1, 2, 3, 2, 0, 65, 21, 4, 2, 10] 
  
 
print ("main list : " + str(list_values)) 
  

# let us  find indices for 2
ans= [i for i in range(len(list_values)) if list_values[i] == 2] 
          
print ("New indices list : " + str(ans)) 
