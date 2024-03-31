def solve_cubic(a, b, c, d):
    # Cubic equation: ax^3 + bx^2 + cx + d = 0

    # Check for special cases
    if a == 0:
        print("This is not a cubic equation.")
        return

    # Calculate discriminant
    delta_0 = b**2 - 3*a*c
    delta_1 = 2*b**3 - 9*a*b*c + 27*a**2*d
    discriminant = delta_1**2 - 4*delta_0**3

    # Define a function to find cube root
    def cube_root(x):
        if x >= 0:
            return x ** (1/3)
        else:
            return -(-x) ** (1/3)

    # Find solutions
    if discriminant > 0:
        # 1 real root, 2 complex roots
        C = cube_root((delta_1 + (delta_1**2 - 4*delta_0**3)**0.5) / 2)
        if C == 0:
            D = 0
        else:
            D = delta_0 / (C * 3)
        x1 = -b / (3 * a) - C - D
        print("One real root and two complex roots:")
        print("x1 =", x1)
        print("x2 =", "(", -b / (3 * a), "+", C, "+", D, "*i )")
        print("x3 =", "(", -b / (3 * a), "-", C, "-", D, "*i )")
    elif discriminant == 0:
        # 3 real roots (at least two are equal)
        if delta_1 == 0:
            K = 0
        else:
            K = delta_1 / (2 * delta_0)
        x1 = -b / (3 * a) - K
        x2 = -b / (3 * a) + K / 2
        x3 = -b / (3 * a) + K / 2
        print("Three real roots (at least two are equal):")
        print("x1 =", x1)
        print("x2 =", x2)
        print("x3 =", x3)
    else:
        # 3 distinct real roots
        C = cube_root((delta_1 + (delta_1**2 - 4*delta_0**3)**0.5) / 2)
        D = delta_0 / (C * 3)
        x1 = -b / (3 * a) - C - D
        x2 = -b / (3 * a) + (C + D) / 2
        x3 = -b / (3 * a) + (C - D) / 2
        print("Three distinct real roots:")
        print("x1 =", x1)
        print("x2 =", x2)
        print("x3 =", x3)

if __name__ == "__main__":
    print("Enter the coefficients of the cubic equation (ax^3 + bx^2 + cx + d = 0):")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    d = float(input("Enter coefficient d: "))
    solve_cubic(a, b, c, d)
