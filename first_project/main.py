import numpy as np


if __name__ == "__main__":
    #1.1
    a1 = np.arange(10)
    print(a1)
    #1.1.1
    a2 = np.arange(100, 201)
    print(a2)
    #1.1.2
    a3 = np.arange(0, 201, 2)
    print(a3)
    #1.1.3
    a4 = np.arange(100, 110.5, 0.5)
    print(a4)
    #1.1.4
    #Gleichverteilt
    a5 = np.random.randint(1, 101, 100)
    print(a5)
    #Normalverteilt
    a6 = np.random.normal(0, 1,100)
    print(a6)

    #2.1
    #Mittelwert
    a7 = np.mean(a6)
    print(a7)
    #Median
    a8 = np.median(a6)
    print(a8)
    #Minimum
    a9 = np.min(a6)
    print(a9)
    #Maximum
    a10 = np.max(a6)
    print(a10)
    #Standartabweichung
    a11 = np.std(a6)
    print(a11)
    #2.2
    for a12 in a6:
        print(a12)
        if a12 >= a7 * 0.025 and a12 <= a7 * 0.975:
            print(a12)
    #2.3
    a13 = a6 * 100
    print(a13)
    #2.4
    a14 = a6[:10]
    print(a14)
    #2.5
    a15 = a6[(a6 > 0)]
    print(a15)