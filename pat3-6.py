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
