#
# ghetto.py
# Bad math library for Python.
#
# Author       : Finn Rayment <finn@rayment.fr>
# Date created : 24/05/2021
#

def floor(x):
	return x // 1

def ceil(x):
	return -floor(-x)
	#return 1 - ((1-x) // 1)

def round(x):
	return floor(2*x+1) // 2
	#return (floor(x) + ceil(x+0.5)) // 2

def ghetto_round_up(x):
	return ((floor(x) + ceil(x-0.5)) // 2) + ceil(x)

def gt0(x):
	i = ghetto_round_up(x)
	return ((2*(i-1) + 2) // (2*(i-1) + 1) + 1) // 2

def geq0(x):
	i = ghetto_round_up(x)
	return ((2*i + 2) // (2*i + 1) + 1) // 2

def gt(x, y):
	return gt0(x-y)

def geq(x, y):
	return geq0(x-y)

def lt0(x):
	i = ghetto_round_up(x)
	return ((2*(i+1) - 2) // (2*(i+1) - 1) + 1) // 2

def leq0(x):
	i = ghetto_round_up(x)
	return ((2*i - 2) // (2*i - 1) + 1) // 2

def lt(x, y):
	return lt0(x-y)

def leq(x, y):
	return leq0(x-y)

def eq(x, y):
	return eq0(x-y)

def neq(x, y):
	return neq0(x-y)

def sign(x):
	return gt0(x) - lt0(x)

def eq0(x):
	return 1 - sign(x) * sign(x)

def abs(x):
	return x * sign(x)

def neq0(x):
	return abs(sign(x))

def min(x, y):
	return (x + y - abs(x - y)) / 2

def max(x, y):
	return (x + y + abs(x - y)) / 2

def clamp(a, b, x):
	return max(a, min(b, x))

def mod(x, y):
	r = x - (y * floor(x/y))
	return neq0(r) * (lt0(x) * (r-y)) + (geq0(x) * r)

