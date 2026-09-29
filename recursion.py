def factorial(n):
    if n == 1 or n== 0:
        return 1
    else:
        return n*factorial(n-1)

def result(n):
    return n

print(result(5))

# print(factorial(5))
# print(factorial(1))
# print(factorial(0))
print(factorial(4))