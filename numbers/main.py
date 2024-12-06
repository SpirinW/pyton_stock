import math as m
class number:
    def __init__(self, a:int=0, rest=0) -> None:
        self.value = a
        self.type = type(a)
        self.even=None
        self.dels=[]
        self.sum = 0
        self.factorial = 0
        self.rest = 0
        self.fraction=None
        self.sign=None
        if a > 0:
            self.sign='positive'
        elif a < 0:
            self.sign='neagtive'
        else:
            self.sign='zero'
        if self.type is int:
            self.even = None if type(a) is not int else a%2 == 0
            self.dels=[] if type(a) is not int else get_dels(a)
            self.prime_dels = get_prime_dels(self.value)
            self.prime_form = get_prime_form(self.value)
            self.rest = rest
            if self.sign == 'positive' and self.value < 6000:
                self.factorial = factorial(self.value)
            
        elif self.type is float:
            self.fraction = get_fraction(self.value)
        self.sum=sum([int(i) for i in str(a).replace('.', '')]) if type(a) in (int, float) else 0
    def __str__(self) -> str:
        res = f'Number: {self.value}\n'
        res += f'Type: {self.type}\n'
        if self.type == int:
            res += f'Even: {self.even}\n'
            res += f'Factorial: {self.factorial}\n'
            res += f'Rest: {self.rest}\n'
            res += f'Divisors: {self.dels}\n'
            res += f'Prime divisors: {self.prime_dels}\n'
            res += f'Prime form: {self.prime_form}\n'
        elif self.type == float:
            res += f'Fraction: {self.fraction}\n'
        res += f'Sum of digits: {self.sum}'
        return res

    def __add__(self, other):
        return number(self.value + other.value)
    def __sub__(self, other):
        return number(self.value - other.value)
    def __mul__(self, other):
        return number(self.value * other.value)
    def __truediv__(self, other):
        return number(self.value / other.value)
    def __floordiv__(self, other):
        return number(self.value // other.value, rest=self.value%other.value)
    def __pow__(self, other):
        return number(self.value ** other.value)
    def __iadd__(self, other):
        self.value += other.value
        return self
    def __isub__(self, other):
        self.value -= other.value
        return self
    def __imul__(self, other):
        self.value *= other.value
        return self
    def __idiv__(self, other):
        self.value /= other.value
        return self
    def __ifloordiv__(self, other):
        self.value //= other.value
        return self
    def __ipow__(self, other):
        self.value **= other.value
        return self

def get_dels(a:int)->list:
    dels = [1]
    for i in range(2, int(m.sqrt(a))+1):
        if a%i == 0:
            dels.append(i)
            if i != a//i:
                dels.append(a//i)
    dels.sort()
    dels.append(a)
    return dels
def is_prime(a:int)->bool:
    for i in range(2, int(a**0.5) + 1):
        if a%i == 0:
            return False
    return True
def get_prime_dels(a:int)->list:
    d = get_dels(a)
    res=[]
    for i in d:
        if is_prime(i):
            res.append(i)
    return res
def get_prime_form(n:int):
    d = get_prime_dels(n)[1:]
    res={}
    i, b = 0, 0
    while(i < len(d) and n!=1):
        if n%d[i] == 0:
            b+=1
            n//=d[i]
        else:
            res[d[i]] = b
            b=0
            i+=1
    res[d[i]]=b
    return res
def nok(a:int, b:int)->int:
    while b!=0:
        a, b = b, a%b
    return a
def nod(a:int, b:int)->int:
    return abs(a*b)//nok(a, b)
def get_fraction(a:float)->tuple:
    if type(a) == int:
        return a, 1
    a, b = str(a).split('.')
    a, b = int(a+b), 10**len(b)
    r = nok(a, b)
    return a//r, b//r
def factorial(n:int):
    if n in (0, 1):
        return 1
    return n*factorial(n-1)
a=number(510)
b = number(431)
print(a)