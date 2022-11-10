from fileOperations import PrimeHandlers
import itertools


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
        self.max = self.handler.getMax()

    def __setSeries(self, first: int, last: int):

        if first >= last:
            return

        if first % 2 == 0:
            if self.__test(first):
                self.series.append(first)
                self.len += 1

            first += 1

        while (first <= last):

            if self.__test(first):
                self.series.append(first)
                self.len += 1

            first += 2

        self.max = last

    def __takeAction(self, number: int):

        status = self.handler.getOrWriteOrAppend(self.min, number)

        if status == 0:
            self.__getSeries()
        elif status == 1:
            self.__setSeries(self.max, number)
            self.handler.writeFile(self.series, self.min, number)
        else:
            k = self.handler.getMax()
            first = k if self.max < k else self.max
            if k == first:
                self.__getSeries()
            ind = len(self.series) - 1
            self.__setSeries(first, number)
            indl = len(self.series)
            self.handler.appendFile(self.series[ind: indl], number)

    def binary_search(self, arr, low, high, x):

        # Check base case
        if high >= low:

            mid = (high + low) // 2

            # If element is present at the middle itself
            if arr[mid] == x:
                return mid

            elif high == low:
                return high

            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)

            # Else the element can only be present in right subarray
            else:
                return self.binary_search(arr, mid + 1, high, x)

        else:
            # Element is not present in the array
            return -1

    def findSeries(self, first: int, last: int):
        if first < 2:
            first = 2

        self.__takeAction(last)

        if first == self.min and last == self.max:
            return self.series.copy()
        else:
            s = self.binary_search(
                self.series, 0, len(self.series) - 1,  first)
            if self.series[s] < first:
                if s + 1 < len(self.series):
                    s += 1

            e = self.binary_search(
                self.series, 0, len(self.series) - 1,  last)
            if self.series[s] > last:
                if e - 1 >= 0:
                    e -= 1

            return self.series[s:e + 1]

    def findPrimeFactors(self, number):

        self.__takeAction(number)

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

        for L in range(len(factors) + 1):

            for subset in itertools.combinations(factors, L):
                mul = 1
                for num in subset:
                    mul *= num
                genPrime.add(mul)

        return list(genPrime)

    def findAllFactors(self, number):

        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)

        return factors

    def getLen(self):
        return self.len
