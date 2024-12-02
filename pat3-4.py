#PROGRAM 4
def sum(a):
    
    str_a=str(a)
    first_dig=int(str_a[0])
    last_dig=int(str_a[-1])
    sum=first_dig+last_dig
    return sum
    
a=1234
print(sum(a))
