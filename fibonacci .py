# By default every fibonacci sequence starts with 0 and 1
x, y = 0, 1
# I am using this count to continue the loop until count is nore than 49
count = 2
# getting the first sum from the first two numbers
sum = 1
while count < 50:
    # reassigning x to be y and y to be x+y
    x, y = y, x+y
    # adding the sum to the sum declared above
    sum = sum + y
    # incrasing our count by 1
    count += 1

# printing out the answer
print('The sum of the first 50 fibonacci sequence is : ', sum)
