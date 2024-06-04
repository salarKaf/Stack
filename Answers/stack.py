class stack:
    def __init__ (self):
        self.stacklist=[]
        self.top=-1
    
    def Push(self , item):
        self.stacklist.append(item)
        self.top=self.top + 1

    
    def IsEmpty(self):
        if(self.top== -1):
            return True
        else:
            return False
    
    def Pop(self):
        if(self.IsEmpty()):
            return self.IsEmpty
        else:
            x= self.stacklist[ self.top]
            del self.stacklist[self.top]
            self.top=self.top-1
            return x
    

    def SizeOfStack(self):
        return len(self.stacklist)
        
    
    def Peek(self):
        if(self.IsEmpty()):
            return "stack Is Empty"
        else:
            x=self.stacklist[self.top]
            return x
    

    def get_max(self):

        max=self.stacklist[0]
        for i in range(1, len(self.stacklist)):
            if(self.stacklist[i] >= max):
                max=self.stacklist[i]
        
        return max
    

# stack = Stack()
# stack.push(100)
# stack.push(10)
# stack.push(20)
# print(stack.get_max) # output: 100
# print(stack.peek()) # Output: 20
# print(stack.pop()) # Output: 20
# print(stack.isEmpty()) # Output: False


# ----------------------------------------------------------------
#Task2
def reverse_string(str):
    s=stack()
    stackReverse=stack()
    for chracter in str:
        s.Push(chracter)
    while(not s.IsEmpty()):
        stackReverse.Push(s.Pop())
    
    return stackReverse.stacklist


# print(reverse_string("hello")) # Output: "olleh"


# ----------------------------------------------------------------
#Task3





# ----------------------------------------------------------------
#Task4
def is_balanced(brackets):
    sForBalavced=stack()
    isBalanced=True
    for b in brackets:
        if( b=="(" or b=="{" or b=="["):
            sForBalavced.Push(b)
        elif( b==")" and (not sForBalavced.IsEmpty() )):
            sForBalavced.Pop()
        elif(b=="}" and (not sForBalavced.IsEmpty() ) ):
            sForBalavced.Pop()
        elif(b=="]" and (not sForBalavced.IsEmpty() )):
            sForBalavced.Pop()
        else:
            isBalanced=False

    if(not sForBalavced.IsEmpty()):
        isBalanced=False  
    return isBalanced
    

# print(is_balanced( "{[()]}"  )) # Output: True
# print(is_balanced(  "({[)"  )) # Output: False


# ----------------------------------------------------------------
#Task5
def prefix_to_postfix(str):

    str =str.split()
    sForOperation=stack()
    for character in str[::-1]:
        if character.isdigit():
            sForOperation.Push(character)
            
        else:
            
            x=sForOperation.Pop()
            y=sForOperation.Pop()
            sForOperation.Push(f"{x} {y} {character}")
    result=sForOperation.Pop() 
    return result

# print(prefix_to_postfix("* + 3 4 2")) # Output: "3 4 + 2 *"

# ----------------------------------------------------------------

#Task6

def sort_stack(stackunsort):
    
    for i in range(stackunsort.SizeOfStack()):
        key=stackunsort.stacklist[i]
        j=i-1
        while(j>=0 and stackunsort.stacklist[j]<key):
            stackunsort.stacklist[j+1]=stackunsort.stacklist[j]
            j=j-1
        stackunsort.stacklist[j+1]=key
    return stackunsort


# s = stack()
# s.Push(3)
# s.Push(1)
# s.Push(4)
# s = sort_stack(s)
# print(s.Pop()) # Output: 1
# print(s.Pop()) # Output: 3


# ----------------------------------------------------------------
#Task7

def infix_to_postfix(str):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    str=str.split()
    StackForOper=stack()
    result=''
    for character in str:
        if character.isdigit():
            result=f"{result} {character}"
        
        else:
            if (StackForOper.IsEmpty()):
                StackForOper.Push(character)
            
            elif(character=="("):
                StackForOper.Push(character)
            
            elif(StackForOper.Peek()=="("):
                StackForOper.Push(character)
            
            
            elif(character==")"):
                while( StackForOper.Peek()!="(" ):
                    result=result + StackForOper.Pop()     
                StackForOper.Pop()


            
            elif(  ( character!=")" ) and  (operators[character] >  operators[StackForOper.Peek()]) ):
                StackForOper.Push(character)
                


            elif((operators[character] <= operators[StackForOper.Peek()]) and (StackForOper.Peek()!="(")):
                while((operators[character] <= operators[StackForOper.Peek()]) and (StackForOper.Peek()!="(")):
                    result=result + StackForOper.Peek()
                    StackForOper.Pop()
                StackForOper.Push(character)

   
    while(not StackForOper.IsEmpty()):
        result=f"{result} {StackForOper.Peek()}"
        StackForOper.Pop()
        

    return result


# print(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 )")) # Output: "3 4 2 * 1 5 - / +"


# ----------------------------------------------------------------

#Task8

def daily_temperatures(listOfTem):
    StackForTem=stack()
    result=[]
    for item in listOfTem[::-1]:
        StackForTem.Push(item)
    while(not StackForTem.IsEmpty()):
        founded=False
        count=0
        tem=StackForTem.Pop()
        t=StackForTem.top
        while(t>=0):
            if(StackForTem.stacklist[t]>tem):
                founded=True
                count=count+1
                break
            t=t-1
            count=count+1
        if(founded):
            result.append(count)
        else:
            result.append(0)

    return result         

# print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73])) # Output: [1, 1, 4, 2, 1, 1, 0, 0]

# ----------------------------------------------------------------            
#Task9



def longestValidParentheses(S):
    mystack=stack()
    ans = 0
    for i in range(len(S)):
        if S[i] == '(':
            mystack.Push(i)
        elif mystack.SizeOfStack == 1:
            mystack[0] = i
        else:
            mystack.Pop()
            ans = max(ans, i - mystack.top)
    return ans


print(longestValidParentheses("(()"))  # خروجی: 2
print(longestValidParentheses(")()())"))  # خروجی: 4


        

            


                



    
    





    
          







        



    


        


