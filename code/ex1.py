'''
#odd or even without division operator
a=int(input("Enter a number: "))
if a&1==0:
  print("Even number")
else:
  print("odd number")
  
'''
def getSum(num):
  if num == 1:
    return 1
  return num + getSum(num-1)

num = 5
print(getSum(num))