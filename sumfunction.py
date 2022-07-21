def sum(num):
    def add(x):
        return num+x
    return add
print(sum(5)(12))        