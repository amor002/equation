try:
	from string import letters
except:
	from string import ascii_letters as letters

def any_of(arr1, arr2):
	for i in arr1:
		for i2 in arr2:
			if i in i2:
				return True, i2
	return False, -1

class Equation:
	numbers = "0123456789"
	operators = {"+": '-', '*': '/', '-': '+', '/': '*'}
	sign = ['+', '-']
	special_operators = "/*"

	def __init__(self, equation, auto_sort=True):
		self.equation = equation
		self.two_sides =  equation.split("=")
		if auto_sort:
			self.sort(self.two_sides[0])

	def sort(self, equation):
		sorted_equation = []
		current_sign = '+'
		check_point = -1
		
		variable = None
		for i in range(len(equation)):
			if i == check_point:
				continue

			if equation[i] in self.numbers and equation[i-1] in self.numbers:
				sorted_equation += [equation[i]]
				continue

			if (equation[i] in self.sign):
				current_sign = equation[i]
			
			
			else:
				if equation[i] not in self.operators:
					sorted_equation += [current_sign+equation[i]]
				else:

					sorted_equation[len(sorted_equation)-1] += equation[i]+equation[i+1]
					check_point = i+1

		
		variable = any_of(letters, sorted_equation)[1] if any_of(letters, sorted_equation)[0] else variable
		sorted_equation = [variable] + (sorted_equation[:sorted_equation.index(variable)] + sorted_equation[sorted_equation.index(variable)+1:])
		self.two_sides[0] = ''.join(sorted_equation)

	def solve(self):
		if self.two_sides[0][2] in self.special_operators:
			try:
				exec("sub_res = " + self.two_sides[0][4:], globals())
			except:
				exec("sub_res = " + self.two_sides[0][4:])
			start = 3
		else:
			try:
				exec("sub_res = " + self.two_sides[0][2:], globals())
			except:
				exec("sub_res = " + self.two_sides[0][2:])
			start = 2

		self.two_sides[0] =  (self.two_sides[0][:4] if start == 3 else self.two_sides[0][:2])+(str(sub_res) if start == 3 and sub_res < 0 else "+"+str(sub_res))
		self.two_sides[0] = self.two_sides[0].replace("+-", '-')
		self.two_sides[1] = self.to_string(self.two_sides[1] + self.reverse(self.two_sides[0][4:])) if start == 3 else self.to_string(self.two_sides[1] + self.reverse(self.two_sides[0][2:]))
		
		self.two_sides[0] = self.two_sides[0][:4]
		self.two_sides[1] = self.to_string(self.two_sides[1] + self.reverse(self.two_sides[0][2:])) if start == 3 else self.two_sides[1]
		exec("self." + self.two_sides[0][1] + '=' + (self.two_sides[1] if self.two_sides[0] != '-' else '-'+self.two_sides[1]))

	def reverse(self, equation):
		equation = list(equation)
		for i in range(len(equation)):
			if equation[i] in self.operators:
				equation[i] = self.operators[equation[i]]

		return ''.join(equation)

	def to_string(self, operation):
		try:
			exec("res = " + operation, globals())
		except:
			exec("res = " + operation)

		return str(res)

#equation1 = Equation("4+x*3-2=8")
#equation1.solve()
#print(equation1.x)
#>>> 2
#equation2 = Equation("y-1=9")
#equation2.solve()
#print(equation2.y)
#>>> 10
