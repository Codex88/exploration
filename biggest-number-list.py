# Looks for the biggest number in a defined list

# set variable for final value to a null (None type)
biggest_num = None
# the list of numbers / dataset
number_list = [3, 8, 9, 47, 21, 19, 82, 24, 37, 56]

# for loop
for i in number_list:
    # checking for None type. Assign first value as first final value
    if biggest_num is None:
        biggest_num = i
    # compare iteration number to final value variable
    if i >= biggest_num:
        biggest_num = i
        # print that a new candidate was found
        print("New biggest number discovered:", i)

# provide the final value
print("Biggest number found:", biggest_num)
