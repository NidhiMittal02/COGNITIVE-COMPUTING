T = (45,89.5,76,45.4,89,92,58,45)
highest = max(T)
print(highest)
highest_index = T.index(highest)
print(highest_index)
lowest = min(T)
print(lowest)
lowest_index = T.index(lowest)
print(lowest_index)
reverse_T= list(T[::-1])
print(reverse_T)
user = 76
if user in T:
    index = T.index(user)
    print("present at index",index)
else:
    print("it's not present")    
