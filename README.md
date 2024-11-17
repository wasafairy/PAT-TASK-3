# PAT-TASK 3
#PROGRAM 1
# function for odd_even
def odd_even(list_a):
    even_list = []
    odd_list = []
    for i in list_a:
        if (i % 2 == 0):
            even_list.append(i)
        else:
            odd_list.append(i)

    print(even_list)
    print(odd_list)


# main program
list_a = [10, 501, 22, 37, 100, 999, 87, 35]
print(odd_even(list_a))



#program 2



numberList = [10,501,22,37,100,999,87,35]
ansList = []
for num in numberList :
    
    if num == 0 or num == 1 :
        continue
        
    for i in range(2, num // 2 + 1) :
 
        if num % i == 0 :
            break
 
    else :
         ansList.append(num)
 
if len(ansList) :
     
    for ans in ansList :
        print([ans])
     
else :
    print("No any number from the given list is Prime")



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
    st = set()
    while (1):
        i = numSquareSum(i)
        if (i == 1):
            return True
        
        
list_a=[10,501,22,37,100,999,87,35]
print(isHappyNumber(list_a))



#PROGRAM 4


  
def sum(a):
    str_a=str(a)
    first_dig=int(str_a[0])
    last_dig=int(str_a[-1])
    sum=first_dig+last_dig
    return sum
    
a=1234
print(sum(a))



#program 6



def dupli(a,b,c):
    set_a=set(a)
    set_b=set(b)
    set_c=set(c)
    
    if (set_a&set_b&set_c):
        return (set_a&set_b&set_c)
    else:
        print("no duplicates")
        
a=[1,2,3,4,5]
b=[1,3,4,5,6]
c=[2,4,5,7,8]
print(dupli(a,b,c))



#program 7



def nonrep(a, n):

    for i in range(n):
        j = 0
        while(j < n):
            if (i != j and a[i] == a[j]):
                break
            j += 1
        if (j == n):
            return a[i]
 
    return -1
 
 
a = [1,2,1,3,2,3,5]
n = len(a)
print(nonrep(a, n))



#program 8



a=[12,52,64,48,26,19,2]
a.sort()      
print("The sorted list is:",a)        
print("\nThe minimum element in the list", a,"is : ",a[0])      

