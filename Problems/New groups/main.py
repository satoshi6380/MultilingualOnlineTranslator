# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
num = int(input())
dict_groups = {}
for i, group in enumerate(groups):
    dict_groups[groups[i]] = int(input()) if i <= num - 1 else None
print(dict_groups)
