# Zinchenko Vlad KI-20010B 
# Variant 5 = 1 task

from random import randint

# variabels
maximum_elements_in_array = 0
our_array = []
our_array_with_negative_numbers = []
max_number_in_array = 0
negative_numbers_exist = False
# variabels


while maximum_elements_in_array < 30:
    our_array.append(randint(-100, 100))

    if our_array[-1] > max_number_in_array:
        max_number_in_array = our_array[-1]

    if our_array[-1] < 0:
        our_array_with_negative_numbers.append(our_array[-1])
        negative_numbers_exist = True


    maximum_elements_in_array += 1


# Output information
print()
print()
print("Our array with numbers between -100, 100")
print(our_array)
print()
print("Maximum in array")
print(max_number_in_array)
print("Index of maximum in array (starts from zero)")
print(our_array.index(max_number_in_array))

if negative_numbers_exist:
    print("Our array with negative numbers sorted")
    print(sorted(our_array_with_negative_numbers, reverse=True) )
else:
    print("No negative numbers in array")
print()