# - Signature will always contain 3 numbers 
# - n will always be a non-negative number
# - if n == 0, then return an empty list and be ready for anything else which is not
# clearly specified ;)

def flatonacci(signature: list, n: int) -> list:
    #This function validate the inputs 
    if validate_input_data(n,signature):
        #If input N get 0 return an empty list
        if n == 0:
            return []
        else:
            #Initializate in 0 the variable as the firt position of the list 
            initial_position=0
            #Get the last position in the list with the len() method
            end_position=len(signature)
            #iteration from last position of the input array until it reaches the level of N 
            while end_position < n:
                #Recolect the add for 0 to 2 in the first iteration, after the add for 1 to 3 and so on
                #Using the sum() function and pass the list encompassing the initial and end position
                #pass the input list using the slicing notation
                total_add = sum(signature[initial_position:end_position])
                #append the total add to the queue of the list 
                signature.append(total_add)
                #one is added to the variable so that it moves to the right 
                initial_position=initial_position+1
                #one is added to the variable so that it moves to the right to the N 
                end_position=end_position+1
                
            #returns the list with each number added 
            return signature

'''Validate the inputs'''
def validate_input_data(n, signature):
    #validate type of N
    if not type(n) is int:
        raise TypeError("N must be integer")
    #Validate N is a positive number
    if n<0:
        raise ValueError("N must be positive integer")
    #Validate the correct length of input list
    if len(signature)<3 or len(signature)>3:
        raise ValueError("Input list must be 3 elements")
    #if all it's OK return True
    return True

'''Control area, call the funcition '''
if __name__ == "__main__":
    #DEfinition of input list
    signature=[-1,-3,5]
    #Length of the output list
    n=8
    #call the function
    print(flatonacci(signature,n))
   


