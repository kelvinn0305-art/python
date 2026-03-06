# li = [23,21,56,89,21]

# Newli = sorted(li)

# print(Newli)
# li.sort()
# print(li)

# li = ["apple","orange","graps","banana"] 

# Newli=sorted(li)
# print(Newli)
# li.sort()
# print(li)

li=[
    {"id":1,"name" :"smit","city" :"rajkot"},
    {"id":2,"name ":"smit","city":"rajkot"},
    {"id":3,"name" :"smit","city":"rajkot"},
    {"id":4,"name" :"smit","city":"rajkot"},
    {"id":5,"name" :"smit","city":"rajkot"}
]

Newli=sorted(li,key=lambda x:x["id"],reverse=True)

print(Newli)