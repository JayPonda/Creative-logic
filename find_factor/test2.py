from find_factores import MathMagic

obj = MathMagic()
print(sorted(obj.findAllFactorsByPrime(1024)))
print(sorted(obj.findAllFactorsByPrime(1056)))
print(sorted(obj.findAllFactorsByPrime(2055)))
print(obj.findPrimeFactors(2059))
print(sorted(obj.findAllFactorsByPrime(2059)))
print(obj.findSeries(2, 2059))
