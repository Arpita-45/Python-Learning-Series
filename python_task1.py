import random
def code1():
    code2=[]
    for a in range(4):
        num=random.randint(0,9)
        code2.append(num)
    return code2

def input_code():
    user_code=input("Enter a four digit code")
    return user_code

def game():
    givencode=code1()
    i=0

    while i<10:
        result=""
        Inputcode=[int(play)for play in input_code() ]
        if len(Inputcode)!=4:
            print("!! Enter a 4 digit code!!")
            continue
        if Inputcode==givencode:
            print("Correct")
            break
        for ele in Inputcode:
            if ele in givencode:
                if Inputcode.index(ele)==givencode.index(ele):
                    result=result+"R"
                else:
                    result=result+"A"
            else:
                result=result+"W"
            print(result)
        i=i+1
    else:
        print("!!Only 10 tries....play again",givencode)
game()
