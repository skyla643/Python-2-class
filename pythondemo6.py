def factorial
   # base case
   if n == 0:
   return 1
# recursive case
else:
return n * factorial(n-1)

def test():
    assert factroial(0) == 1
    assert factorial(1)  == 1
    assert factorial(2)  == 2
    assert factorial(3)  == 3
    assert factorial(4)  == 4
    assert factorial(5)  == 5
    assert factorial(10)  == 3628800

    print("All test cases passed!") 

test() 