"""
    Para medir la complejdad ciclomática del código
    ejecutar el comando: radon cc <path>

    A un lado de cada archivo se mostrará una letra:

    1 - 5	A (low risk - simple block)
    6 - 10	B (low risk - well structured and stable block)
    11 - 20	C (moderate risk - slightly complex block)
    21 - 30	D (more than moderate risk - more complex block)
    31 - 40	E (high risk - complex block, alarming)
    41+	F (very high risk - error-prone, unstable block)

    https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity

"""


def func_class_a():
    dato = ""
    for i in range(0, 3):
        dato += "-"


def func_class_b():
    for i in range(0, 10):
        for j in range(0, 5):
            print(f"i: j")
            if (j < 3):
                if (i < 3):
                    print("QUE COSA 3 de 3")
                    for jj in range(0, i):
                        print("----")

        for pp in range(0, 100):
            for ppp in range(0, 4):
                print("asd")


# Código con muchos riesgos clase C
global_bad = "OO"


def func_class_c():
    for i in range(0, 10):
        for j in range(0, 5):
            print(f"i: j")
            if (j < 3):
                global_bad = 23
                if (i < 3):
                    print("QUE COSA 3 de 3")
                    for jj in range(0, i):
                        print("----")
                        global_bad = "AAA"
                        if (global_bad == "OO"):
                            for te in range(0, 9):
                                global_bad = True

        for pp in range(0, 100):
            for ppp in range(0, 4):
                print("asd")
            for sksks in range(10, 12):
                global_bad = False
