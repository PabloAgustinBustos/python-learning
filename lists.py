import sys

users = ["Pablo", "alvaro", "Juan", "sebas", "Lucas", "Agus", "Eze", "José"]

users.sort(key=str.lower)

print(users)

nums = [4, 42, 78, 1, 5]
nums.sort(reverse=True)     # Mutable
print(nums)

num2 = [4, 9, 1, 2]
print(sorted(nums))         # Inmutable

ages = [23, 21, 26, 34, 28]
agesReference = ages        # Toma la referencia, por tanto, modificará a la lista original

agesReference.append(20)

print(ages)

ages2 = ages[:]             # Copia los elementos. Son listas diferentes

print(sys.getsizeof('a'))