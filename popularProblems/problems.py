# A stack is a linear data structure in which you can use push to put data in and 
# pop to take data out in a LIFO order. So push puts something on top of stack
# while pop takes something out of top of stack. 

# Popular methods: 
# .isEmpty() returns true is stack is empty.
# .length() returns length of stack.
# .top() returns pointer or reference to top item in stack. 
# .push() add to top of stack.
# .pop() remove from top of stack. 

class Solution: 
   def isValid(self, s: str) -> bool: 
        stack = []
        for i in s:
            if i not in ')]}':
                stack.append(i)

            elif stack:
                x = stack.pop()
                if (x == '(' and i != ')') or (x == '[' and i != ']') or (x == '{' and i != '}'):
                    return False

            else:
                return False

        return False if stack else True
        
    
