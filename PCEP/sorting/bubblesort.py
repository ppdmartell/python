# This bubblesort works with two loops, the for loop will be executing until reaching len
# but then the while loop will set the variable to False over and over. And as long there
# is a swap, the swapped variable will be set to True. This ensures the sorting algorithm
# will behave as bubbles coming from bottom to the surface, unless there is a bubble they
# can't surpass.


list = [7,5,8,1,9,2]
print(list)
swapped = True

while swapped:
    swapped = False
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            swapped = True
            list[i], list[i + 1] = list[i + 1], list[i]

print(list)
