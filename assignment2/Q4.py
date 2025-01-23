A={34,56,78,90}
B={78,45,90,23}
union_score = A.union(B)
print(union_score)
intersection_score = A.intersection(B)
print(intersection_score)
symmteric_difference = A.symmetric_difference(B)
print(symmteric_difference)
subset = A.issubset(B)
print(subset)
superset = B. issuperset(A)
print(superset)
X = int(input("enter the any number:"))
if X in A:
    print("present in set A")
else:
    print("not present in set A")