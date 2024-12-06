from polynomial import *
def test(input_name):
	file = open("input.txt")
	result = open("test_result.txt", "w")
	test_number = 1
	for line in file:
		p=poly([float(i) for i in line.split()])
		ans = "Test N{}:\nFor equation \n{} = 0\n{}\n".format(test_number, p, solve(p))
		print(ans)
		result.write(ans)
		test_number+=1

def test_signle(a:list):
	p=poly([float(i) for i in a])
	print("For equation \n{} = 0\n{}".format(p, solve(p)))


#print(quadric_solve(0.1, -1, -5*11*277))
#test("input.txt")
'''
a=[3, 4, -2, 0]
test_signle(a)
a=root(1, 0)
b=root(1, 1)
sol = solution([a, b])

print(sol)
a=[
[1, -2, -1, 1],
[5, -8, -8, 5],
[5, -1, -20, 4],
[1, 0, -2, 1]]
for i in a:
	test_signle(i)
for i in [1.0000000000000004, -1.9999999999999998, 1.9999999999999998, 1.9999999999999999, 0.19999999999999818, -0.9999999999999999]:
	temp = i
	floor_correct(temp)
	print(i , temp)
inaccurate:

test_signle(a)
print(cubic_solve(1, -1, -1, 1))
print(quatic_solve(1, -1, -1, 1, 0))
print(quatic_solve(1, 3, 2, 10, 0))
print(cubic_solve(1, 4, 13, 10))
print(cubic_solve(4, 3, 2, 1))
print(cubic_solve(1, 3, 2, 10))
print(quadric_solve(1, 10, 0.037037037037037035))
test_signle([1,2,3,4, -1])

'''
set_plot_info(-50, 50, 1)
f=poly([7, -20, 4, -2, 20, -1000])
print(f)
f.plot()