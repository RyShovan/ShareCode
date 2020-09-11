"""
Script Concept by Pritam.
"Let's write a script which will give us the iterate number of
every unique element in that list"
"""

name_list = ["Anari", "kamal", "Bahana", "Ana", "Partha", "kamal", "Bahana", "Bahana", "Bahana"]
repeat_dict = {}

for i in name_list:
    k = 0
    for j in range(len(name_list)):
        if i == name_list[j]:
            k += 1
    repeat_dict[i] = k

print(repeat_dict)
