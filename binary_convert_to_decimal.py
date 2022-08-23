# I imported random which will help me to make a selection from a list.
import random

# I have a list of all binary numbers with 4 digits
mylist = ["0000", "0001", "0010", "0011", "0100", "0101", "0110",
          "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]

# here I ma making a selection which will choose and item from the list
selection = random.choice(mylist)
# Here I am converting the selected binary number to base 10 using the int()
decimal_eqvivalence = int(selection, 2)
# printing the answer
print('The base 10 eqivalence of '+selection+' is : '+str(decimal_eqvivalence))
