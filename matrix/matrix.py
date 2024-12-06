class matrix(object):
	def __init__(self, a="empty"):
		if type(a) == list:
			correct = True
			if len(a) == 0:
				self.a=[[]]
				return 
			size = len(a[0])
			for i in a:
				correct*= size == len(i)
			if correct:
				self.a =[]
				for i in a:
					self.a.append([float(k) for k in i])
				self.times_swaped = 0
			else:
				self.a=[[]]
		elif type(a) == int or type(a) == float:
			self.a=[[a]]
		elif type(a) == matrix:
			self.a=a.a
		elif a == "empty":
			self.a=[[]]
	def size(self):
		return [len(self.a), len(self.a[0])]
	def simplify(self):
		a=self.a
		for i in range(len(a)):
			if a[i][i] == 0:
				k = 0
				while(k < len(a)-1 and a[k][i] == 0):
					k+=1
				a[k], a[i] = a[i], a[k]
				self.times_swaped+=1
		for k in range(len(a)):
			for i in range(k+1, len(a)):
				if a[k][k]:
					m = a[i][k]/a[k][k]
					for j in range(k, len(a[k])):
						a[i][j] -= m*a[k][j] 
		self.a = a
	def transpose(self):
		trans_a=[[0 for j in range(len(self.a))] for i in range(len(self.a[0]))]
		for i in range(len(self.a)):
			for j in range(len(self.a[0])):
				trans_a[j][i] = self.a[i][j]
		self.a=trans_a
	def det(self):
		if self.size()[0] != self.size()[1]:
			return 0
		a=simplified(self).a
		d=1 if simplified(self).times_swaped%2 == 0 else -1
		for i in range(len(a)):
			d*=a[i][i]
		return d
	def solve(self):
		if self.size()[0] != self.size()[1]-1:
			return []
		self.simplify()
		temp = matrix([row[:-1] for row in self.a])
		if temp.det() == 0:
			return []
		x = [0]*self.size()[0]
		for i in range(self.size()[0]-1, -1, -1):
			s = self.a[i][-1]
			print(f'for {i} row:')
			for k in range(self.size()[1]-2, i, -1):
				print(s, x[k], self.a[i][k])
				s -= x[k]*self.a[i][k]
			x[i] = s/self.a[i][i]
		return x
	
	def rank(self):
		a=simplified(self).a
		r=len(a)
		for i in range(len(a)):
			if a[i][i] == 0:
				r-=1
		return r
	def get_minor(self, a = int, b = int):
		res=[]
		for i in range(len(self.a)):
			temp=[]
			for j in range(len(self.a[i])):
				if i != a and j != b:
					temp.append(0.0 if self.a[i][j] == -0.0 or self.a[i][j] == 0.0 else self.a[i][j])
			if len(temp):
				res.append(temp)
		return matrix(res)  
	def get_alg_dop(self, a = int, b = int):
		res = float(self.get_minor(a,b).det())
		return res if (a+b)%2 == 0 else res*(-1)
	def get_alg_matrix(self):
		a=[]
		for i in range(len(self.a)):
			a.append([self.get_alg_dop(i, j) for j in range(len(self.a[0]))])
		return transposed(matrix(a))
	def __str__(self):
		if len(self.a[0]) == 0:
			return "Your matrix is empty"
		m = self.a[0][0]
		res=""
		for i in self.a:
			m = max(m, max(i))
		for i in self.a:
			for j in i:
				res+=str(j if j != -0.0 else 0.0).ljust(len(str(m)), ' ') + ' '
			res+='\n'
		return res[:-1]
	def __add__(self, other):
		if type(self) == matrix and type(other) == matrix and self.size() == other.size():
			res=[]
			for i in range(self.size()[0]):
				temp=[]
				for j in range(self.size()[1]):
					temp.append(self.a[i][j] + other.a[i][j])
				res.append(temp)
			return matrix(res)
	def __sub__(self, other):
		if type(other) == matrix and type(self) == matrix:
			return self + other*(-1)
	def __mul__(self, other):
		if type(self) == matrix and type(other) == int or type(other) == float:
			res=[]
			for i in self.a:
				temp=[]
				for j in i:
					temp.append(j*other)
				res.append(temp)
			return matrix(res)
		elif type(self) == matrix and type(other) == matrix and self.size()[1] == other.size()[0]:
			res=[]
			for i in range(self.size()[0]):
				temp=[]
				for j in range(other.size()[1]):
					s=0
					for k in range(self.size()[1]):
						s+=self.a[i][k]*other.a[k][j]
					temp.append(s)
				res.append(temp)
			return matrix(res)
	def __rmul__(self, other):
		if type(other) == int or type(other) == float:
			return self*other
	def __pow__(self, power):
		if self.size()[0] != self.size()[1]:
			return None	
		if type(power) == int:
			if power == 0:
				a=[[int(i == j) for j in range(self.size()[0])] for i in range(self.size()[0])]
				return matrix(a)
			elif power > 0:
				if power == 1:
					return self
				else:
					a=self
					for _ in range(power-1):
						a=a*self
					return a
			else:
				if power == -1:
					return self.get_alg_matrix()*(1/self.det())
				else:
					return (self**-1)**power
		if type(power) == float:
			fract = get_fraction(power)
			return (self**fract[0])*((self**fract[1])**(-1))
def simplified(a = matrix):
	res=matrix(a.a)
	res.simplify()
	return res
def transposed(a = matrix):
	res=matrix(a.a)
	res.transpose()
	return res
def get_common_denominator(fract = tuple):
	for i in range(2, max(fract)):
		if fract[0]%i == 0 and fract[1]%i == 0:
			return i
	return 0
def get_fraction(x):
	if type(x) == int:
		return (x, 1)
	elif type(x) == float:
		first=last=""
		check=False
		for i in str(x):
			if i == '.':
				check=True
			else:
				if not check:
					first+=i
				else:
					last+=i
		fract = (int(first+last), 10**(len(last)))
		r=get_common_denominator(fract)
		while(r != 0):
			fract = (fract[0]//r, fract[1]//r)
			r=get_common_denominator(fract)
		return fract