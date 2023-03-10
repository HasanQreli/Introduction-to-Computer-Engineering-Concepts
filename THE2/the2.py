studentNumber = input()
checkDigit= studentNumber[5:]
if checkDigit == "X":
    checkDigit =10

if "?" not in studentNumber:
    if (2*int(studentNumber[0])+3*int(studentNumber[1])+5*int(studentNumber[2])+7*int(studentNumber[3]))%11 == int(checkDigit):
        print('VALID')
    else:
        print('INVALID')

elif checkDigit == '?':
    checkDigit = (2*int(studentNumber[0])+3*int(studentNumber[1])+5*int(studentNumber[2])+7*int(studentNumber[3]))%11
    if checkDigit == 10:
        print(studentNumber[0:5]+"X")
    else:
        print(studentNumber[0:5]+str(checkDigit))

elif "?" == studentNumber[0]:
    a = int(((int(checkDigit)-3*int(studentNumber[1])-5*int(studentNumber[2])-7*int(studentNumber[3]))%11+(((int(checkDigit)-3*int(studentNumber[1])-5*int(studentNumber[2])-7*int(studentNumber[3]))%11)%2)*11)/2)
    print(str(a)+studentNumber[1:])

elif "?" == studentNumber[1]:
    b = int(((int(checkDigit)-2*int(studentNumber[0])-5*int(studentNumber[2])-7*int(studentNumber[3]))%11+(((int(checkDigit)-2*int(studentNumber[0])-5*int(studentNumber[2])-7*int(studentNumber[3]))%11)%3)*11)/3)
    print(str(studentNumber[0])+str(b)+studentNumber[2:])

elif "?" == studentNumber[2]:
    c = int(((int(checkDigit)-2*int(studentNumber[0])-3*int(studentNumber[1])-7*int(studentNumber[3]))%11+(abs((((int(checkDigit)-2*int(studentNumber[0])-3*int(studentNumber[1])-7*int(studentNumber[3]))%11)-15))%5)*11)/5)
    print(studentNumber[0:2]+str(c)+studentNumber[3:])

elif "?" == studentNumber[3]:
    d = int(((int(checkDigit)-2*int(studentNumber[0])-3*int(studentNumber[1])-5*int(studentNumber[2]))%11+(abs((((int(checkDigit)-2*int(studentNumber[0])-3*int(studentNumber[1])-5*int(studentNumber[2]))%11)*5))%7)*11)/7)
    print(studentNumber[0:3]+str(d)+studentNumber[4:])