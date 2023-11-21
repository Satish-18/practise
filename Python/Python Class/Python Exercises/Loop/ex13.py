#Write code that will iterate over the range starting at 1, up to but not including 11, with a step of 2,
#and for each element that is between 3 and 8 inclusively print out the result of multiplying that element 
#by the last element in the same range. For any other element of the range (outside [3-8]) print Outside!

for i in range(1,11,2):
    if 3 <= i <= 8:
        print(i * range(1,11,2)[-1])
    else:
        print("Outside!")