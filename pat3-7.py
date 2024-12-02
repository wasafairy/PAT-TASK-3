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
 
 
a = [1,1,3,2,3,5]
n = len(a)
print(nonrep(a, n))
