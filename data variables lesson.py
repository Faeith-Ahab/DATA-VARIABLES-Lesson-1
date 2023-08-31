#integers(int)
tall_men = 40
TotalAmount = 300
newTotalAmount = str(TotalAmount)
Total = int(newTotalAmount)

#type casting integers
#print(type(newTotalAmount)) #int to str
#print(type(Total))

#strings (str)
currency ="UGX"
payment ="Your payment is " + currency + " " + str(TotalAmount)
message = """ 
Read up about operators ie concatention operators, pascal naming, snake case, type casting, define integers and strings, how to comment, naming convetions, syntax

"""

#strings are array like structures meaning the first character of a string starts with 0
for a in "apple":
    print(a)

#boolean (bool)
HasAttended = True
IsMale = False


# the output
print(payment)
print("Your payment is UGX" " " + newTotalAmount)

