n=int(input("Enter number: "))
def print_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
print_fact(n)