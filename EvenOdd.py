number = int(input("Enter a number: "))
def check_eo(num):
  if num % 2 == 0:
    return (num, "is even")
  else:
    return (num, "is odd")
check_eo(number)
