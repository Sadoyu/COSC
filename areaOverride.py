class Shape(object):
	def area(length):
		return 0
	class Square(object):
		def __init__(self, length):
			self.length = length
		def area(length):
			return length**2
side = int(input("Enter the length of the side of the Square: "))
a = 0
a = area(side)
print(a)
