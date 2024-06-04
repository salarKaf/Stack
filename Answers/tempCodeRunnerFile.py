else:
            if (StackForOper.IsEmpty()):
                print("first op"+character)
                StackForOper.Push(character)
            
            elif(  ( character!=")" ) and  (operators[character] >  operators[StackForOper.Peek()]) ):
                print("normal op"+character)
                StackForOper.Push(character)

            elif( operators[character] <= operators[StackForOper.Peek()] ):
                print("priority op"+character)
                while(operators[character]<operators[StackForOper.Peek()]):
                    print("priority op"+character)
                    result=f"{result} {StackForOper.Peek()}"
                    StackForOper.Pop()
                    print(StackForOper.Peek())
                StackForOper.Push(character)

            elif(character==")"):
                # print("op"+character)
                while( StackForOper.Peek()!="(" ):
                    result=f"{result} {StackForOper.Peek()}"
                    StackForOper.Pop()
                StackForOper.Pop()
