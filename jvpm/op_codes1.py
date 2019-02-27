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

'''
	def OP_code60(self, data):
                var1 = data.pop() + data.pop()
		push_to_stack(self, data, var1)

	def OP_code7e(self, data):
		var1 = data.pop() & data.pop()
		push_to_stack(self, data, var1)

	def OP_code6c(self, data):
		var1 = data.pop() / data.pop()
		push_to_stack(self, data, var1)

	def OP_code68(self, data):
		var1 = data.pop() * data.pop()
		push_to_stack(self, data, var1)

	def OP_codes74(self, data):
		var1 = data.pop() * -1
		push_to_stack(self, data, var1)

	def push_to_stack(self, data, result):
		data.push(result) '''
