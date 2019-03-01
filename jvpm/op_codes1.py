'''
All Methods for OP Codes go in this file
'''

class op_codes:

        def op_code70(stack_z):     #remainder
                var1 = stack_z.pop() % stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code78(stack_z):     #shift left
                var1 = stack_z.pop() << stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code80(stack_z):     #bitwise OR
                var1 = stack_z.pop() | stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code05(stack_z):        #loads 2 onto stack
                stack_z.append(2)
                return stack_z

        def op_code06(stack_z):        #loads 3 onto stack
                stack_z.append(3)
                return stack_z

        def op_code07(stack_z):        #loads 4 onto stack
                stack_z.append(4)
                return stack_z

        def op_code08(stack_z):        #loads 5 onto stack
                stack_z.append(5)
                return stack_z

        def op_code60(stack_z): # add
                MAX_JAVA_INT = 2147483647
                MIN_JAVA_INT = -2147483647
                var1 = stack_z.pop()
                var2 = stack_z.pop()

                if (var1 > MAX_JAVA_INT or var2 > MAX_JAVA_INT):
                        var1 += var2
                        var1 += MIN_JAVA_INT
                elif (var1 < MIN_JAVA_INT and var2 < MIN_JAVA_INT):
                        var1 += var2
                        var1 += MAX_JAVA_INT
                else:
                        var1 += var2

                stack_z.append(var1)
                return stack_z

        def op_code7e(stack_z): # bitwise and
                var1 = stack_z.pop() & stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code6c(stack_z): # integer division
                var1 = stack_z.pop() // stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code68(stack_z): # multiplication
                var1 = stack_z.pop() * stack_z.pop()
                stack_z.append(var1)
                return stack_z

        def op_code74(stack_z): # change to negative
                var1 = stack_z.pop() * -1
                stack_z.append(var1)
                return stack_z

        def op_code02(stack_z): # loads -1 into the stack
                stack_z.append(-1)
                return stack_z

        def op_code03(stack_z): # loads 0 into the stack
                stack_z.append(0)
                return stack_z

        def op_code04(stack_z): # loads 1 into the stack
                stack_z.append(1)
                return stack_z