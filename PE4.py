#PE4
#04/07/2016
#906609

def palindrome(n):
    return str(n)==str(n)[::-1]
    
def largest_palindrome_product_3():
    maxi=(0,0,0)
    for i in range(100,1000):
        for j in range(100,1000):
            if i*j>maxi[0] and palindrome(i*j):
                maxi=(i*j,i,j)
    return maxi
