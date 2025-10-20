import Frac

"""
x = Frac.Frac(2,5)
x.show()

z = Frac.Frac(1,3)
y = x.mult(z)

y.show()
"""

a = Frac.Frac(4,5)
b = Frac.Frac(3,5)

a.mult(b).show()
a.div(b).show()
a.soma(b).show()
a.subtracao(b).show()


a.show(a.mult(a.div(a.subtracao(a.soma(b)))))