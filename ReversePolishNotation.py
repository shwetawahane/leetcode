class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) ==1:
            return tokens[0]
        
        arr = []
        arr.append(tokens[0])
        arr.append(tokens[1])
        for i in range(2,len(tokens)):
            
            current = tokens[i]    
            #x = checkOp(current)
            
            try:
                num = int(current)
                x = True
            except:
                x = False
            
            if x:
                arr.append(current)
            else:
                first = arr.pop()
                second = arr.pop()
                #result = Operate(first, second, current)
                
                if current == "+":
                    result= int(first) + int(second)
                elif current == "-":
                    result= int(second) - int(first)
                elif current == '*':
                    result= int(second) * int(first)
                elif current == '/':
                    result = int(int(second) / int(first))
                    '''
                    if int(first) < 0 and int(second) < 0:
                        result= int(second) // int(first)
                    if int(first) < 0 or int(second) < 0: 
                        result = round(int(second) / int(first))
                    else:
                        result= int(second) // int(first)
                   '''
           
                    
                arr.append(result)
                # print(result, arr)
        return arr[0]
'''    
    def checkOp(op):
        try:
            num = int(op)
            return True
        except:
            return False
   
    def Operate(first,second,current):
        current = str(current)
        if current == "+":
            return first + second
        elif current == "-":
            return second - first
        elif current == '*':
            return second * first
        elif current == '/':
            return second / first
'''
