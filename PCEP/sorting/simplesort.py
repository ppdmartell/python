# Contrary to what I thought, this is not bubble sort. Probably has a name which I most
# likely will find out at some point, but basically is brute-forcing comparing each element
# to the rest. Time complexity should be n^2.


list = [8,10,6,2,4]
print(list)

for i in range(len(list) - 1):
    for j in range(len(list)):
        if list[i] < list[j]:
            list[i], list[j] = list[j], list[i]

print(list)
