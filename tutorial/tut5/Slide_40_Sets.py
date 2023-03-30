numberSet = {1, 2, 5, 7, 8, 10}
anotherNumberSet = {1, 3, 5, 10, 18, 21}
# numberSet3 = {1, 3, 5, 10, 18, 21}

union = numberSet.union(anotherNumberSet)
# OR
union = numberSet | anotherNumberSet
print(union)

intersection = numberSet.intersection(anotherNumberSet)
# OR
intersection = numberSet & anotherNumberSet
print(intersection)

difference = numberSet.difference(anotherNumberSet)
# OR
difference = numberSet - anotherNumberSet
print(difference)

symmetric = numberSet.symmetric_difference(anotherNumberSet)
# OR
symmetric = numberSet ^ anotherNumberSet
print(symmetric)


# print(numberSet.issubset(numberSet2))
# print(numberSet3.issubset(numberSet3))
# print(5 in numberSet)
# numberSet = set()
# numberSet.add("One")
# print(numberSet)
# numberSet.remove("One")
# numberSet.discard("Two")