import time
import numpy as np
import random
from fileOperations import PrimeHandlers


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




