import time


class MathMagic():

    def __init__(self) -> None:
        self.series = []
        self.min = 2
        self.max = 2
        self.len = 0

    def __test(self, n):
        for min in self.series:
            if n % min == 0:
                return False
        return True

    def findSeries(self, first: int, last: int):
        if first < 2:
            first = 2

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
        return self.series

    def findPrimeFactors(self, number):

        if self.max < number:
            self.findSeries(self.max, number)

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


obj = MathMagic()
testNumber = 1265 * 161
print(testNumber, testNumber + 5000, testNumber - 5000)

# test 1
print("\ntest 1: find series, comparing new val with prime")
k = time.time_ns()
print(obj.findSeries(0, testNumber), obj.getLen())
k1 = time.time_ns()

print((k1 - k) * (10 ** -9))

# test 2
print("\ntest 2: find prime factors, comparing and dividing with prime")
k = time.time_ns()
print(obj.findPrimeFactors(testNumber), obj.getLen())
k1 = time.time_ns()

print((k1 - k) * (10 ** -9))

# test 2.1
print("\ntest 2.1: find prime factors, comparing and dividing with prime")
k = time.time_ns()
lis = obj.findPrimeFactors(testNumber + 5000)
print(lis, obj.getLen())
k1 = time.time_ns()

print((k1 - k) * (10 ** -9))

# test 2.2
print("\ntest 2.2: find prime factors, comparing and dividing with prime")
k = time.time_ns()
lis = obj.findPrimeFactors(testNumber + 5000)
print(lis, obj.getLen())
k1 = time.time_ns()

print((k1 - k) * (10 ** -9))

# test 2.3
print("\ntest 2.3: find prime factors, comparing and dividing with prime")
k = time.time_ns()
lis = obj.findPrimeFactors(testNumber - 5000)
print(lis, obj.getLen())
k1 = time.time_ns()

print((k1 - k) * (10 ** -9))

# test 3
print("\ntest 3: find prime factors, comparing and dividing with prime set")
k = time.time_ns()
print(set(lis), obj.getLen())
k1 = time.time_ns()

print((k1 - k) * (10 ** -9))

# test 4
print("\ntest 4: find all factors, checking")
k = time.time_ns()
lis = obj.findAllFactors(testNumber + 5000)
print(lis)
k1 = time.time_ns()

print((k1 - k) * (10 ** -9))

# test 5
print("\ntest 5: find prime factors, checking for prime from all factors set")
k = time.time_ns()
print(obj.findPrimeFactorsOptimisedSet(lis))
k1 = time.time_ns()

print((k1 - k) * (10 ** -9))
