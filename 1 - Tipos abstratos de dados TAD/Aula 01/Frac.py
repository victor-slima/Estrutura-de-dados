class Frac:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador
    
    def show(self):
        print(self.num,"/",self.den)
    
    def mult(self, m):
        n = self.num * m.num
        d = self.den * m.den
        t = Frac(n, d)
        return t
    
    def div(self, d):
        n = self.num * d.den
        de = self.den * d.num
        t = Frac(n, de)
        return t
    
    def soma(self, sm):
        if self.den == sm.den:
            n = self.num + sm.num
            d = self.den
        else:
            n = (self.num * sm.den) + (self.den * sm.num)
            d = self.den * sm.den
        return Frac(n, d)
    
    def subtracao(self, ss):
        if self.den == ss.den:
            n = self.num - ss.num
            d = self.den
        else:
            n = (self.num * ss.den) - (self.den * ss.num)
            d = self.den * ss.den
        return Frac(n, d)

# estudar o self, tudo na verdade.
# subindo esse trem.