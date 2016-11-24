def fibonacci(n,k):
    if n==1 or n==2:
         return 1
    else:
        fibo = fibonacci(n-1,k)+k*fibonacci(n-2,k)
    print fibo
    return  fibo

n = input("Enter the Value of n: ")
k= input("Enter the value of k: ")
fibonacci(n,k)