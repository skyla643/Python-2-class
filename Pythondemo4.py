def factorial(number):
   if number == 0: # base case handler
    return 1
else:
    return number * factorial(number - 1)

results = factorial(5)
print(results)