def Fibonacci(num1, num2):  # this pattern continues to 10th number
    num3 = num1 + num2
    num4 = num2 + num3
    num5 = num3 + num4
    num6 = num4 + num5
    num7 = num5 + num6
    num8 = num6 + num7
    num9 = num7 + num8
    num10 = num8 + num9
    print(
        f"output:\n{num1}, {num2}, {num3}, {num4}, {num5}, {num6}, {num7}, {num8}, {num9}, {num10}")


def Cube(figor):
    result = figor * figor * figor
    print(f"output:\n{result}")


def Square(figor):
    result = figor * figor
    print(f"output:\n{result}")


def Triangle(figor):
    result = (figor * (figor + 1)) / 2
    print(f"output:\n{result}")


def Pentecostal(figor):  # To Arabic: مخمسی
    result = (figor * (3 * figor - 1)) / 2
    print(f"output:\n{result}")


def My_Pistol(figor):  # To Arebic: مسدسی
    result = figor * ((2 * figor) - 1)
    print(f"output:\n{result}")
