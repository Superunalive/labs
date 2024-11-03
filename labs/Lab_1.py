
import sys

def read_input(n, messg):
    try:
        coef = sys.argv[n]
    except:
        print(messg)
        coef = input()
    try:
        coef = float(coef)
    finally:
        return coef
    
def calculations(A, B, C): #Ax^4 + Bx^2 + C = 0, A != 0
    results = []
    if B*B - 4*A*C < 0:
        return results
    elif B*B - 4*A*C == 0:
        if -B/2*A > 0:
            results.append((-B/2*A)**0.5)
            results.append(-(-B/2*A)**0.5)
        else:
            results.append(0)
    else: # root = +-sqrt(-b +- sqrt(D)/2a)
        if (-B + (B*B - 4*A*C)**0.5)/A < 0:
            return results
        elif -B + (B*B - 4*A*C)**0.5 == 0 or -B - (B*B - 4*A*C)**0.5 == 0:
            results.append(0)
        else:
            results.append(((-B + (B*B - 4*A*C)**0.5)/(2*A))**0.5)
            results.append(-((-B + (B*B - 4*A*C)**0.5)/(2*A))**0.5)
        if (-B - (B*B - 4*A*C)**0.5)/A > 0:
            results.append(((-B - (B*B - 4*A*C)**0.5)/(2*A))**0.5)
            results.append(-((-B - (B*B - 4*A*C)**0.5)/(2*A))**0.5)
    return results


def main():
    A = read_input(1, "Input coefficient A:")
    B = read_input(2, "Input coefficient B:")
    C = read_input(3, "Input coefficient C:")
    
    while (type(A) != float or type(B) != float or type(C) != float):
        print("One of the inputs is incorrect, please try again")
        A = read_input(4, "Input coefficient A:")
        B = read_input(4, "Input coefficient B:")
        C = read_input(4, "Input coefficient C:")
    if A == 0:
        print("This is not a biquadratic equation. Here is the solution anyway:")
        if B == 0 and C == 0:
            print("all real numbers are solutions")
        elif (B == 0 and C != 0) or (B*C > 0):
            print("no real solution exist")
        else:
            print("2 roots:", (-C/B)**0.5, -(-C/B)**0.5)
    else:
        roots = calculations(A, B, C)
        if len(roots) == 0:
            print("no real solution exist")
        else:
            print(len(roots), "roots:", roots)
        
main()
