lst_str = input(" Enter list elements separated by space: ")
lst1 = lst_str.split()            # Converting string into list
dict_frequency = dict()           # Creating empty dictionary to store the no. of occurrences of each element

for i in lst1:
    if i not in dict_frequency: 
        dict_frequency[i] = 1
    else:
        dict_frequency[i] += 1
print("No. of times each element has occured in the list: ", dict_frequency)

