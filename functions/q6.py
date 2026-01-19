def find_case(s):
    uppercase = 0
    lowercase = 0
    for ch in s:
        if(ch.isupper()):
            uppercase+=1
        elif(ch.islower()):
            lowercase+=1
    print("number of uppercase in this string ",uppercase)
    print("number of lowercase in this string ",lowercase)
print(find_case("this is a strinG"))            