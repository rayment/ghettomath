#
# ghetto.py
# Bad math library for Python.
#
# Author       : Finn Rayment <finn@rayment.fr>
# Date created : 24/05/2021
#

PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406
E  = 2.718281828459045235360287471352662497757247093699959574966967627724076630

def floor(x):
	return x // 1

def ceil(x):
	return -floor(-x)
	#return 1 - ((1-x) // 1)

def round(x):
	return floor(2*x+1) // 2
	#return (floor(x) + ceil(x+0.5)) // 2

def _dir(x):
	#return ((floor(x) + ceil(x-0.5)) // 2) + ceil(x)
	return floor(x) + ceil(x)

def gt0(x):
	i = _dir(x)
	return ((2*(i-1) + 2) // (2*(i-1) + 1) + 1) // 2

def geq0(x):
	i = _dir(x)
	return ((2*i + 2) // (2*i + 1) + 1) // 2

def gt(x, y):
	return gt0(x-y)

def geq(x, y):
	return geq0(x-y)

def lt0(x):
	i = _dir(x)
	return ((2*(i+1) - 2) // (2*(i+1) - 1) + 1) // 2

def leq0(x):
	i = _dir(x)
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

def round_down(x):
	return floor(abs(x)) * sign(x)

def round_up(x):
	return ceil(abs(x)) * sign(x)

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

def ln(x):
	t = (x-1)/(x+1)
	t2 = t*t
	p = (91/93)*t2*(1 + (93/95)*t2*(1 + (95/97)*t2*(1 / (1 - 97/99*t2))))
	o = (85/87)*t2*(1 + (87/89)*t2*(1 + (89/91)*t2*(1 + p)))
	n = (79/81)*t2*(1 + (81/83)*t2*(1 + (83/85)*t2*(1 + o)))
	m = (73/75)*t2*(1 + (75/77)*t2*(1 + (77/79)*t2*(1 + n)))
	l = (67/69)*t2*(1 + (69/71)*t2*(1 + (71/73)*t2*(1 + m)))
	k = (61/63)*t2*(1 + (63/65)*t2*(1 + (65/67)*t2*(1 + l)))
	j = (55/57)*t2*(1 + (57/59)*t2*(1 + (59/61)*t2*(1 + k)))
	i = (49/51)*t2*(1 + (51/53)*t2*(1 + (53/55)*t2*(1 + j)))
	h = (43/45)*t2*(1 + (45/47)*t2*(1 + (47/49)*t2*(1 + i)))
	g = (37/39)*t2*(1 + (39/41)*t2*(1 + (41/43)*t2*(1 + h)))
	f = (31/33)*t2*(1 + (33/35)*t2*(1 + (35/37)*t2*(1 + g)))
	e = (25/27)*t2*(1 + (27/29)*t2*(1 + (29/31)*t2*(1 + f)))
	d = (19/21)*t2*(1 + (21/23)*t2*(1 + (23/25)*t2*(1 + e)))
	c = (13/15)*t2*(1 + (15/17)*t2*(1 + (17/19)*t2*(1 + d)))
	b = (7/9)*t2*(1 + (9/11)*t2*(1 + (11/13)*t2*(1 + c)))
	a = 2*t*(1 + (1/3)*t2*(1 + (3/5)*t2*(1 + (5/7)*t2*(1 + b))))
	return a

def logn(x, n):
	return ln(x) / ln(n)

def log2(x):
	return logn(x, 2)

def log(x):
	return logn(x, 10)

def sin(x):
	a = round_down(x / (PI))
	b = abs(x - a*PI)
	c = (neq0(mod(a, 2)) * -1) + eq0(mod(a, 2))
	d = (16*b*(PI-b))/((5*PI*PI)-4*b*(PI-b))
	return d * sign(x) * c

def cos(x):
	return sin(x+(PI/2))

def tan(x):
	return sin(x) / cos(x)

