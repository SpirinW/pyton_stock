import math
import matplotlib.pyplot as plt
epsilon = 10**-6

def set_plot_info(min=-200, max=200, step=1):
	global plot_info
	plot_info={'min':min, 'max':max, 'step':step}
set_plot_info()
def sign (a):
	if(a == 0):
		return ''
	if(a > 0):
		return '+'
	else:
		return '-'

def too_small(a: float):
	return a <= epsilon

def floor_correct(a: float):
	if a > 0:
		if abs(a - (int(a) + 1)) <= epsilon:
			a=int(a) + 1
		elif abs(a - (int(a) - 1)) <= epsilon:
			a=int(a) - 1
		elif abs(a - int(a)) <= epsilon:
			a=int(a)
	elif a < 0:
		if abs(a - (int(a) + 1)) <= epsilon:
			a=int(a) + 1
		elif abs(a - (int(a) - 1)) <= epsilon:
			a=int(a) - 1
		elif abs(a - int(a)) <= epsilon:
			a=int(a)

class root(object): # aprox here
	def __init__(self, a=0.0, b=0.0):
		if(type(a) == complex):
			self.real=a.real
			self.imag=a.imag
		elif(type(a) == root):
			self = a
		else:
			self.real = a
			if b != 0:
				self.imag = b
			else:
				self.imag = 0
			if abs(self.real) <= 10**-6:
				self.real=0
			elif abs(self.imag) <=10**-6:
				self.imag=0
	def is_complex(self):
		return self.imag != 0
	def real(self):
		return float(self.real)
	def __str__(self):
		if self.imag != 0:
			if self.real != 0:
				ans="{} {} {}i".format(self.real if self.real != 0 else '', sign(self.imag), abs(self.imag) if self.imag != 1 else '')
			else:
				ans="{}i".format(self.imag)
		else:
			ans = "{}".format(self.real)
		return ans
	def __add__(self, other):
		if (type(other) == float or type(other) == int):
			res = root(self.real + other, self.imag)
		elif (type(other) == root):
			res = root(self.real + other.real, self.imag + other.imag)
		return res
	def __sub__(self, other):
		if (type(other) == float or type(other) == int):
			res = root(self.real - other, self.imag)
		elif (type(other) == root):
			res = root(self.real - other.real, self.imag - other.imag)
		return res
	def __mul__(self, other):
		if type(other) == float or type(other) == int:
			res = root(self.real*other, self.imag*other)
			return res
		elif type(other) == root:
			res = root(self.real*other.real - self.imag*other.imag, self.real*other.imag + other.real*self.imag)
			return res
	def __pow__(self, power):
		if not self.is_complex:
			res = root(self.real**power)
			return res
		else:
			if(power == 0.5):
				a, b = self.real, self.imag
				x = (0.5*((a*a+b*b)**0.5 + a))**0.5
				y = (0.5*((a*a+b*b)**0.5 - a))**0.5 
				if(b < 0):
					res = root(x, -y)
				else:
					res = root(x, y)
				return res
	def __eq__(self, other):
		return self.real == other.real and self.imag == other.imag
	def __gt__(self, other):
		if self.imag == 0 and other.imag == 0:
			return self.real > other.real
		elif self.imag == 0 and other.imag != 0:
			return True
		elif self.imag != 0 and other.imag == 0:
			return False
		else:
			a1, b1, a2, b2 = self.real, self.imag, other.real, other.imag
			return (a1*a1 + b1*b1)**0.5 > (a2*a2 + b2*b2)**0.5 
	def __lt__(self, other):
		if self.imag == 0 and other.imag == 0:
			return self.real < other.real
		elif self.imag == 0 and other.imag != 0:
			return False
		elif self.imag != 0 and other.imag == 0:
			return True
		else:
			a1, b1, a2, b2 = self.real, self.imag, other.real, other.imag
			return (a1*a1 + b1*b1)**0.5 < (a2*a2 + b2*b2)**0.5 
	def __ge__(self, other):
		return self > other or self == other
	def __le__(self, other):
		return self < other or self == other

class solution(object):
	def __init__(self, a: list[root]):
		self.all_roots=[]
		for i in a:
			if i not in self.all_roots:
				k=0
				while(k < len(self.all_roots) and i > self.all_roots[k]):
					k+=1
				self.all_roots.insert(k, i)
	def get_real_roots(self):
		res=[]
		for i in self.all_roots:
			if not i.is_complex():
				res.append(i)
		return res
	def get_complex_roots(self):
		res=[]
		for i in self.all_roots:
			if i.is_complex():
				res.append(i)
		return res	
	def __str__(self):
		ans = ""
		real, comp = self.get_real_roots(), self.get_complex_roots()
		if len(real):
			ans += "{} real ".format(len(real))
		if len(comp):
			ans +="{}{} complex ".format(',' if len(real) > 0 else '', len(comp))
		ans="There {} ".format('are' if len(real)+len(comp) > 1 else 'is') + ans + "solution{}:\n".format('s' if len(real)+len(comp) > 1 else '')
		for i in real:
			ans+="{}\n".format(i)
		for i in comp:
			ans+="{}\n".format(i)
		return ans[:len(ans)-1]
	def __add__(self, other):
		r=self.all_roots+other.all_roots
		return solution(r)
	def __getitem__(self, i: int):
		return self.all_roots[i]

class poly(object):
	def __init__(self, a):
		if type(a) == list:
			self.q = a
			self.order = len(self.q) -1
			while(self.order != 0 and self.q[len(self.q) - self.order - 1] == 0):
				self.order-=1
	
	def calc(self, a):
		if type(a) == int or type(a) == float:
			res=0.0
			for i in range(self.order+1):
				res+=self.q[i]*a**i
			return res
	
	def plot(self):
		x=list(range(plot_info['min'], plot_info['max']+1))
		y=[self.calc(i) for i in x]
		plt.plot(x, y)
		plt.show()
	
	def scatter(self):
		x=list(range(plot_info['min'], plot_info['max']+1))
		y=[self.calc(i) for i in x]
		plt.scatter(x, y)
		plt.show()

	def __str__(self):
		for i in range(len(self.q)):
			if self.q[i]%1 == 0:
				self.q[i]=int(self.q[i])
		if self.order == 0:
			return str(self.q[0])
		ans=""
		for i in range(len(self.q)):
			if i == 0:
				if self.q[i] != 0:
					ans+="{}{}x^{} ".format('-' if sign(self.q[i]) == '-' else '', abs(self.q[i]) if abs(self.q[i]) != 1 else '', self.order - i)
			elif i == len(self.q) - 1:
				if(self.q[i] != 0):
					ans+="{} {}".format(sign(self.q[i]), abs(self.q[i]))
			elif i == len(self.q) - 2:
				if(self.q[i] != 0):
					ans+="{} {}x ".format(sign(self.q[i]), abs(self.q[i]) if abs(self.q[i]) != 1 else '')
			else:
				if(self.q[i] != 0):
					ans+="{} {}x^{} ".format(sign(self.q[i]), abs(self.q[i]) if abs(self.q[i]) != 1 else '', self.order - i)
		return ans
	
	def __add__(self, other):
		r=[(0.0) for i in range(max(self.order, other.order) +1)]
		for i in range(min(len(self.q), len(other.q))):
			r[len(r) - i -1]=self.q[len(self.q) - i -1] + other.q[len(other.q) - i - 1]

		for i in range(min(len(self.q), len(other.q)), max(len(self.q), len(other.q))):
			if(self.order > other.order):
				r[len(r) - i - 1]=self.q[len(self.q) - i - 1]
			else:
				r[len(r) - i - 1]=other.q[len(other.q) -i - 1]
		return poly(r)
	
	def __mul__(self, other):
		if type(other) == int or type(other) == float:
			res=[float(i) for i in self.q]
			for i in range(len(res)):
				res[i]*=other
			return poly(res)
		if(type(other) == poly):
			r=[(0.0) for i in range(self.order + other.order +1)]
			for i in range(self.order+1):
				for j in range(other.order+1):
					r[i+j]+=self.q[i]*other.q[j]
			res=poly(r)
			return res
	
	def __sub__(self, other):
		if type(other) == int or type(other) == float:
			self.q[len(self.q) - 1]-=other
			res=self
			return res
		if type(other) == poly:
			res=self + (other*(-1))
			return res
	
	def __pow__(self, a):
		if type(a) == int and a >= 0:
			if a==0:
				res=poly([1])
				return res
			else:
				res=poly([1])
				while(a):
					res*=self
					a-=1
				return res
	
	def __getitem__(self, i: int):
		if i >= 0:
			return self.q[i]
		else:
			return self.q[len(self.q) - abs(i) - 1]
	
	def __iadd__(self, other):
		self=self+other
	
	def __isub__(self, other):
		self=self+other*(-1)

def quadric_solve(a: float, b: float, c: float):
	D, a_1= b*b - 4*a*c, 1/a
	if D == 0:
		return solution([root(-0.5*b*a_1, 0)])
	elif D > 0:
		#print("D=",D)
		x1,x2=root(0.5*a_1*(D**0.5 - b)), root(0.5*a_1*(-(D**0.5) - b))
		#print(x1, x2)
		return solution([x1,x2])
	else:
		return solution([root(-0.5*b*a_1, 0.5*a_1*(-D)**0.5), root(-0.5*b*a_1, -0.5*a_1*(-D)**0.5)])

def complex_quadric_solve(b: root, c: root):
	D_1 = (b*b*0.25 - c)**0.5
	if D_1.real == 0 and D_1.imag == 0:
		return solution([b*0.5])
	else:
		x1, x2 = D_1 - b*0.5, D_1*(-1) -b*0.5
		return solution([x1, x2])

def cubic_solve(a: float, b: float, c: float, d: float):
	if (d == 0):
		solution_1 = quadric_solve(a, b, c)
		return solution(quadric_solve(a, b, c).all_roots + [root(0)])
	one_third, two_seven, root_3, a_1, a_3 = 1/3, 1/27, 3**0.5, 1/a, 1/(a*a*a)
	#ax^3 + bx^2 + cx + d => y^3 + py + q
	p = (3*a*c - b*b)*one_third*a_3*a
	q = (2*b*b*b - 9*b*c*a + 27*a*a*d)*two_seven*a_3
	if q == 0:
		if p == 0: 
			return solution([root(-b*one_third*a_1)])
		else:
			x=[root(-b*one_third*a_1)]
			if (p <= 0):
				x.append(root((-p)**0.5 - b*one_third*a_1))
				x.append(root(-(-p)**0.5 - b*one_third*a_1))
				return solution(x)
			else:
				return solution(x + [root(0, p**0.5), root(0, -p**0.5)]) 
	else:
		if p == 0:
			return solution([root(-q**one_third), root(0.5*q**one_third, 0.5*root_3*q**one_third), root(0.5*q**one_third, -0.5*root_3*q**one_third)])
		else:#x^3 + px + q => z^6 + qz^3 -(p^3)/27 = 0
			solution_z = quadric_solve(1, q, -p*p*p*two_seven)
			z_roots=solution_z.get_real_roots()
			if(len(z_roots) == 2 or len(z_roots) == 1): # 2 real roots from f(z)

				z=z_roots[0].real
				if z >= 0:
					z=z**one_third
				else:
					z=-(-z)**one_third
				z_re, z_im = -0.5*z, 0.5*root_3*z
				y_re, y_im = z_re - z_re*one_third*p/(z_re*z_re + z_im*z_im), z_im + one_third*z_im*p/(z_re*z_re + z_im*z_im)
				x=[z - one_third*p/z - one_third*a_1*b, y_re - one_third*a_1*b, y_im]
				if x[2] == 0:
					return solution([root(x[0]), root(x[1])])
				return solution([root(x[0]), root(x[1], x[2]), root(x[1], -x[2])])
			else:
				cos = 1.5*root_3*q/(p*(-p)**0.5)
				ang = math.acos(cos)*180/math.pi
				psy=[ang*one_third, ang*one_third+120, ang*one_third +240]
				r = (abs(p)*one_third)**0.5
				x=[0.0]*3
				for i in range(3):
					x[i] = (r - one_third*p/r)*math.cos(psy[i]*math.pi/180)
				return solution([root(x[0] - b*one_third*a_1), root(x[1] - b*one_third*a_1), root(x[2] - b*one_third*a_1)])

def quatic_solve(a: float, b: float, c: float, d: float, e:float):
	a_1=1/a
	if b == 0 and d == 0: #ax^4 + cx^2 + e = 0 => (x^2 + b_1x + c_1)(x^2 - b_1x + c_1)
		c, e = c*a_1, e*a_1
		c_1= root(e, 0)
		c_1=c_1**0.5
		b_1=root(c_1.real, c_1.imag)
		b_1.real=b_1.real*2 - c
		b_1.imag=b_1.imag*2
		b_1=b_1**0.5
		solution_1, solution_2 = complex_quadric_solve(b_1, c_1), complex_quadric_solve(b_1*(-1), c_1)
		return solution_1 + solution_2
	elif d == 0 and e == 0: # ax^4 + bx^3 + cx^2=0 => ax^2 + bx + c=0 + x = 0
		solution_1 = quadric_solve(a, b, c)
		return solution([root(0)] + solution_1.all_roots)
	elif e == 0: # ax^4 + bx^3 + cx^2 + dx=0 => ax^3 + bx^2 + cx + d=0 + x = 0  
		solution_1 = cubic_solve(a, b, c, d)
		if root(0) in solution_1.all_roots:
			return solution_1
		return solution([root(0)] + solution_1.all_roots)
	a_4, one_eight, one_third = a_1*a_1*a_1*a_1, 0.125, 1/3
	p = (8*a*c - 3*b*b)*a*a*a_4*one_eight
	q = (b*b*b - 4*b*c*a + 8*d*a*a)*one_eight*a_4*a
	r = (256*a*a*a*e - 3*b*b*b*b + 16*a*b*b*c - 64*a*a*b*d)*one_eight*one_eight*one_eight*2*a_4
	if p == 0 and q ==0 and r == 0:
		return solution([root(-b*0.25*a_1)])
	elif q == 0:
		#(root(i) - 0.25*b*a_1) for i in quatic_solve(1, 0, p, 0, r).all_roots
		solution_1_roots = []
		for i in quatic_solve(1, 0, p, 0, r).all_roots:
			solution_1_roots.append(i - 0.25*b*a_1)
		return solution(solution_1_roots)
	solution_w, k = cubic_solve(8, -8*r, 4*p*r, -q*q), 0
	w = solution_w.get_real_roots()[k].real
	if len(solution_w.get_real_roots()) == 3:
		while(2*w - p <= 0):
			w=solution_w.get_real_roots()[k].real
			k+=1
	if 2*w-p >= 0:
		f = (2*w - p)**0.5
		g = -q/f*0.5
		solution_1 = quadric_solve(1, -f, w - g)
		solution_2 = quadric_solve(1, f, w + g)
		res = []
		#(root(i) - 0.25*b*a_1) for i in (solution_1.all_roots + solution_2.all_roots)
		for i in (solution_1.all_roots + solution_2.all_roots):
			res.append(i - 0.25*b*a_1)
		return solution(res)
	else:
		for i in (solution_1.all_roots + solution_2.all_roots):
			res.append(i - 0.25*b*a_1)
		return solution(res)

def solve(p: poly):
	if len(p.q) == 3:
		result = quadric_solve(p[0], p[1], p[2])
	elif len(p.q) == 4:
		result = cubic_solve(p[0], p[1], p[2], p[3])
	elif len(p.q) == 5:
		result = quatic_solve(p[0], p[1], p[2], p[3], p[4])
	return result 
