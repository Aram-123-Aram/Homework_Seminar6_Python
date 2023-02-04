list = [34, 2, 67, 45, 23, 1]
'''
#variant1
list = [list[i] for i in range(len(list)) if i%2!=0]

print(list)
def sum(list3):
    summa=0
    for x in list3:
        summa+=x
    return summa
print(sum(list))
'''


list = [list[i] for i in range(len(list)) if i%2!=0]
print(list,"->")
print("sum =", sum(list[::]))
'''
#variant3
print(sum(list[1::2]))
'''