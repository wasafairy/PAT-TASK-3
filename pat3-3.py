#program 3
def numSquareSum(list_a):
    num = 0
    for i in list_a:
        while(i):
            digit = i % 10
            num = num + digit*digit
            i= i // 10
        return num


def isHappyNumber(i):
    happy_no=0
    a=0
    st = set()
    while (1):
        i = numSquareSum(i)
        if (i == 1):
            a+=1
            return a
        
        
list_a=[10,501,22,37,100,999,87,35]
print("THE NUMBER OF HAPPY NUMBERS IN THE GIVEN LIST : ",isHappyNumber(list_a))
