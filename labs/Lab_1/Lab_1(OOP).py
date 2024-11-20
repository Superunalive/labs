import sys

class BiQuadEquation:
    
    def __init__(self):
        self.A = 0.0
        self.B = 0.0
        self.C = 0.0
        self.roots = []
        self.num_roots = 0
    
    def get_coef(self, n, messg):
        try:
            coef = sys.argv[n]
        except:
            print(messg)
            coef = input()
        try:
            coef = float(coef)
        finally:
            return coef
        
    def get_coefs(self):
        self.A = self.get_coef(1, "Input coefficient A:")
        self.B = self.get_coef(2, "Input coefficient B:")
        self.C = self.get_coef(3, "Input coefficient C:")
        
        while (type(self.A) != float or type(self.B) != float or type(self.C) != float):
            print("One of the inputs is incorrect, please try again")
            self.A = self.get_coef(4, "Input coefficient A:")
            self.B = self.get_coef(4, "Input coefficient B:")
            self.C = self.get_coef(4, "Input coefficient C:")
            
    def calc_roots(self):
        a, b, c = self.A, self.B, self.C
        D = b**2 - 4*a*c
        self.roots = [] #resetting roots to calculate
        self.num_roots = 0
        
        if D < 0:
            self.roots = []
            self.num_roots = 0
        elif D == 0:
            if -b/2*a > 0:
                self.roots.append((-b/2*a)**0.5)
                self.roots.append(-(-b/2*a)**0.5)
                self.num_roots += 2
            else:
                self.roots.append(0)
                self.num_roots += 1
        else: # root = +-sqrt(-b +- sqrt(D)/2a)
            if (-b + (b*b - 4*a*c)**0.5)/a < 0:
                return self.roots
            elif -b + D**0.5 == 0 or -b - D**0.5 == 0:
                self.roots.append(0)
                self.roots.num_roots += 1
            else:
                self.roots.append(((-b + D**0.5)/(2*a))**0.5)
                self.roots.append(-((-b + D**0.5)/(2*a))**0.5)
                self.num_roots += 2
            if (-b - D**0.5)/a > 0:
                self.roots.append(((-b - D**0.5)/(2*a))**0.5)
                self.roots.append(-((-b - D**0.5)/(2*a))**0.5)
                self.num_roots += 2
        return self.roots
        
    def print_roots(self):
        if self.num_roots == 0:
            print("no real solution exist")
        else:
            print(self.num_roots, "roots:", self.roots)
            
def main():
    eq = BiQuadEquation()
    
    eq.get_coefs()
    eq.calc_roots()
    eq.print_roots()
    
main()