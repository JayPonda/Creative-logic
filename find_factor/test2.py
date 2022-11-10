from find_factores import MathMagic


obj = MathMagic()
print(sorted(obj.findAllFactorsByPrime(1024)))
print(sorted(obj.findAllFactorsByPrime(1056)))
print(sorted(obj.findAllFactorsByPrime(2055)))
print(obj.findPrimeFactors(204))
print(sorted(obj.findAllFactorsByPrime(204)))
print(obj.findAllFactors(204))
print(obj.findSeries(2, 2059))
