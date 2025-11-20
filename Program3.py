input=int(input("Enter a number:"))

if input%2==0:
  input-=1
result=[]

for i in range(1,input+1):
  odd=2*i-1
  result.append(odd)
print(result)
