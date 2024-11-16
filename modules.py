import math
import sys
import package

print("{:.2f}".format(math.pi))

for item in dir(package):
    print(item)

print()

print(package.num)
package.increment()
print(package.num)
package.increment(5)
print(package.num)

print()

print(__name__)
print(package.__name__)

if __name__ == "__main__":
    print("Hola")