def factorial
   # base case
   if n == 0:
   return 1
# recursive case
else:
return n * factorial(n-1)

def test():
    test_cases *{
        (0,1), 
        (1,1),
        (2,2),
        (3,6),
        (4,24),
        (5,120),
        (6,720),
        (7,5040),
        (8,40320),
        (9,362880),
        (10,3628800)<
    }
for n, expected in test_cases:
    result = factorial(n)
    print(f"factorial({n}) = {result}. expected = {expected}") 
    if result == expected
       print("test passed")
else:
    print("test failed")
test() 