def HelloUser(username): #<-- 2) Go to here. username = "Sam"
    sentence = ("Hello {0}, we hope you've enjoyed using this very simple function").format(username) #<-- 3) Assign Sentence
    return sentence #<-- 4) We return Sentence HelloName now = sentence

HelloName = HelloUser("Sam") #<-- 1) Exection starts here <-- 5) We return to here
print(HelloName) #<-- 6) We print out helloName which now = sentence.


def modifyMultiple(value1,value2):
    value1 += 10
    value2 += 5
    return value1,value2

value1 = 10
value2 = 15

value1,value2 = modifyMultiple(value1,value2)

print(value1)
print(value2)
