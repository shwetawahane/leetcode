''' 150. Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. 
That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''

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
