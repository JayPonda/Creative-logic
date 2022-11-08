import time
import numpy as np
import random
import matplotlib.pyplot as plt
from fileOperations import PrimeHandlers
import os


class MathMagic():

    def __init__(self) -> None:
        self.series = []
        self.handler = PrimeHandlers('PrimeList', 'PrimeConfig')
        self.min = 2
        self.max = 2
        self.len = 0

    def __test(self, n: int):
        for min in self.series:
            if n % min == 0:
                return False
        return True

    def __getSeries(self):
        self.series = self.handler.readFile()

    def __setSeries(self, first: int, last: int):

        if first >= last:
            return

        if first % 2 == 0:
            if self.__test(first):
                self.series.append(first)
                self.len += 1

            first += 1

        while (first < last):

            if self.__test(first):
                self.series.append(first)
                self.len += 1

            first += 2

        self.max = last

    def findSeries(self, first: int, last: int):
        if first < 2:
            first = 2
        temp = []

        if first % 2 == 0:
            if self.__test(first):
                temp.append(first)

            first += 1

        while (first < last):

            if self.__test(first):
                temp.append(first)

            first += 2

        return temp

    def findPrimeFactors(self, number):

        status = self.handler.getOrWriteOrAppend(self.min, number)

        if status == 0:
            self.__getSeries()
        elif status == 1:
            self.__setSeries(self.max, number)
            self.handler.writeFile(self.series, self.min, number)
        else:
            k = self.handler.getConfig()['max']
            first = k if self.max < k else self.max
            if k == first:
                self.__getSeries()
            ind = len(self.series) - 1
            self.__setSeries(first, number)
            indl = len(self.series)
            self.handler.appendFile(self.series[ind: indl], number)

        newVal = number
        factors = []

        while (newVal > 1):

            for prime in self.series:
                if (prime > newVal):
                    break

                if newVal % prime == 0:
                    newVal /= prime
                    factors.append(prime)
                    break

        return factors

    def findAllFactorsByPrime(self, anyObj):
        if isinstance(anyObj, list):
            factors = anyObj
        elif isinstance(anyObj, int):
            factors = self.findPrimeFactors(anyObj)

        genPrime = set([1])

        for i in range(len(factors) + 1):

            for j in range(i + 1, len(factors) + 1):

                mul = 1

                for v in range(i, j):
                    mul *= factors[v]

                genPrime.add(mul)

        return list(genPrime)

    def findPrimeFactorsOptimisedSet(self, number):
        if isinstance(number, list):
            factores = number
        else:
            factores = self.findAllFactors(number)

        def checkForPrime(number):
            for i in range(2, number):
                if number % i == 0:
                    return False
            return False if number == 1 else True

        return list(filter(lambda x: checkForPrime(x), factores))

    def findAllFactors(self, number):

        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)

        return factors

    def getLen(self):
        return self.len


def printTest(ar, tn):

    arcs = ar
    tests = np.zeros(arcs, dtype=int)
    testNumber = tn

    testResults1 = np.zeros(arcs, dtype=float)
    testResults2 = np.zeros(arcs, dtype=float)
    interwal: int = testNumber / arcs
    obj = MathMagic()

    for i in range(arcs):

        xNumber = random.randint((i * interwal) + 1, (i + 1) * interwal)
        tests[i] = xNumber
        # print(xNumber)

        # test 1
        # print("\ntest 1: find prime factors, comparing and dividing with prime")
        k = time.time_ns()
        set(obj.findAllFactorsByPrime(testNumber))
        k1 = time.time_ns()

        testResults1[i] = (k1 - k) * (10 ** -9)

        # test 2
        # print("\ntest 2: find prime factors, checking for prime from all factors set")
        k = time.time_ns()
        lis = obj.findAllFactors(testNumber)
        k1 = time.time_ns()

        testResults2[i] = (k1 - k) * (10 ** -9)

    del lis
    del obj

    avg1 = np.round(np.mean(testResults1), 5)
    first = testResults1[0]
    testResults1[0] = testResults1[1]
    plt.axes()
    plt.plot(tests, testResults1, '-.', label=f"testResults1: {avg1} sec")
    avg = np.round(np.mean(testResults2), 5)
    plt.plot(tests, testResults2, '-o', label=f"testResults2: {avg} sec")
    plt.title(
        f"find prime series gen ({np.sum(testResults1)} sec) + gen factors vs try all factors ({np.sum(testResults2)} sec)")
    print(f"secondary avg: {(first + np.mean(testResults1)) / 2}")

    plt.legend()
    return (np.round(np.sum(first), 7),
            np.round(np.sum(testResults1), 7),
            np.round(np.sum(testResults2), 7))
    plt.show()
    plt.savefig('testplot' + str(np.random.randint(1, 1000)) + '.png')


# for i in range(3, 5):
#     k = printTest(1000, i * 10000)
#     os.remove('PrimeList.txt')
#     os.remove('PrimeConfig.json')
#     k1 = printTest(1000, i * 10000)
#     print(f"""
#     <tr>
#         <th rowspan="3">{i + 2}</th>
#         <td>New</td>
#         <td>{i * 10000}</td>
#         <td>1000</td>
#         <td>{k1[0]}</td>
#         <td>{k1[1]}</td>
#         <td>{k1[2]}</td>
#     </tr>
#     <tr>
#         <td>Append</td>
#         <td>{i * 10000}</td>
#         <td>1000</td>
#         <td>{k[0]}</td>
#         <td>{k[1]}</td>
#         <td>{k[2]}</td>
#     </tr>
#     """)
#     k = printTest(1000, i * 10000)
#     print(f"""
#     <tr>
#         <td>Stored</td>
#         <td>{i * 10000}</td>
#         <td>1000</td>
#         <td>{k[0]}</td>
#         <td>{k[1]}</td>
#         <td>{k[2]}</td>
#     </tr>
#     """)
