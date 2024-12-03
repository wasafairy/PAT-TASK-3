# PAT-TASK 3
#PROGRAM 1
# function for odd_even
def odd_even(list_a):
    even_list = []
    odd_list = []
    for i in list_a:
        if (i % 2 == 0):
            even_list.append(i)
        else:
            odd_list.append(i)

    print(even_list)
    print(odd_list)


# main program
list_a = [10, 501, 22, 37, 100, 999, 87, 351]
print(odd_even(list_a))
