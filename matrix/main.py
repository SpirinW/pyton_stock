from matrix import * 
def get_matrix_from_file(filename = str):
	with open(filename, 'r') as file:
		res=[]
		for row in file.readlines():
			res.append([float(i) for i in row.split()])
		return matrix(res)
a=get_matrix_from_file("input.txt")
#print(a)
#a.simplify()
#print(get_fraction(-26.714285714285715))
#print(get_fraction(563.678))
'''
print(a)
print(a.det())
print("===========")
print(a**-1)
'''


