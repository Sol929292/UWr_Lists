"""
Zad. 3
Zaprogramuj funkcję romb(n), która wypisze romb o wysokości 2 ∗ n − 1. Poniżej
przykład takiego rombu dla wywołania romb(4):
1234#
123###
12#####
1#######
#########
 #######
  #####
   ###
    #

"""

n = 4

def romb(n):
    for i in range(0, n+1):
        print((n-i)*" ",(2*i+1)*"#")
    for i in range(n-1, -1, -1):
        print((n-i)*" ",(2*i+1)*"#")

romb(n)