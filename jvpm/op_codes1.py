'''
All Methods for OP Codes go in this file
'''

class op_codes:
        def op_code70(x,y):     #remainder
                return x%y

        def op_code78(x,y):     #shift left
                return x<<y

        def op_code80(x,y):     #bitwise OR
                return x|y

        def op_code05():        #loads 2 onto stack
                self.stack_z.append(2)
                return 2

        def op_code06():        #loads 3 onto stack
                self.stack_z.append(3)
                return 3

        def op_code07():        #loads 4 onto stack
                self.stack_z.append(4)
                return 4

        def op_code08():        #loads 5 onto stack
                self.stack_z.append(5)
                return 5

        def op_code60(stack_z): # add
                var1 = stack_z.pop() + stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code7e(stack_z): # bitwise and
                var1 = stack_z.pop() & stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code6c(stack_z): # integer division
                var1 = stack_z.pop() / stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code68(stack_z): # multiplication
                var1 = stack_z.pop() * stack_z.pop()
                stack_z.append(var1)
                return stack_z

	    def op_codes74(stack_z): # change to negative
		        var1 = stack_z.pop() * -1
		        stack_z.append(var1)
                return stack_z

