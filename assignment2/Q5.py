sample_dict = {"name": "Kelly", "age":25, "salary":8000, "city":"New york"}
old_key = "city"
new_key = "location"
sample_dict[new_key]= sample_dict.pop(old_key)
print(sample_dict)