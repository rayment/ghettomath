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

def exp(x):
	p = x+81-(81*x/(x+82-(x*82/(x+83-(83*x/(x+84-(84*x/(x+85))))))))
	o = x+76-(76*x/(x+77-(x*77/(x+78-(78*x/(x+79-(79*x/(x+80-(80*x/p)))))))))
	n = x+71-(71*x/(x+72-(x*72/(x+73-(73*x/(x+74-(74*x/(x+75-(75*x/o)))))))))
	m = x+66-(66*x/(x+67-(x*67/(x+68-(68*x/(x+69-(69*x/(x+70-(70*x/n)))))))))
	l = x+61-(61*x/(x+62-(x*62/(x+63-(63*x/(x+64-(64*x/(x+65-(65*x/m)))))))))
	k = x+56-(56*x/(x+57-(x*57/(x+58-(58*x/(x+59-(59*x/(x+60-(60*x/l)))))))))
	j = x+51-(51*x/(x+52-(x*52/(x+53-(53*x/(x+54-(54*x/(x+55-(55*x/k)))))))))
	i = x+46-(46*x/(x+47-(x*47/(x+48-(48*x/(x+49-(49*x/(x+50-(50*x/j)))))))))
	h = x+41-(41*x/(x+42-(x*42/(x+43-(43*x/(x+44-(44*x/(x+45-(45*x/i)))))))))
	g = x+36-(36*x/(x+37-(x*37/(x+38-(38*x/(x+39-(39*x/(x+40-(40*x/h)))))))))
	f = x+31-(31*x/(x+32-(x*32/(x+33-(33*x/(x+34-(34*x/(x+35-(35*x/g)))))))))
	e = x+26-(26*x/(x+27-(x*27/(x+28-(28*x/(x+29-(29*x/(x+30-(30*x/f)))))))))
	d = x+21-(21*x/(x+22-(x*22/(x+23-(23*x/(x+24-(24*x/(x+25-(25*x/e)))))))))
	c = x+16-(16*x/(x+17-(x*17/(x+18-(18*x/(x+19-(19*x/(x+20-(20*x/d)))))))))
	b = x+11-(11*x/(x+12-(x*12/(x+13-(13*x/(x+14-(14*x/(x+15-(15*x/c)))))))))
	a = x+6-(6*x/(x+7-(x*7/(x+8-(8*x/(x+9-(9*x/(x+10-(10*x/b)))))))))
	return 1 + x/(1 - x/(x+2-(2*x)/(x+3-(3*x)/(x+4-(4*x/(x+5-(5*x/(a))))))))

