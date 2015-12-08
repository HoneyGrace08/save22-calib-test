#numbers  = range(1,101)
#numbers = list(numbers)

#sum = 0
#for i in numbers:
#  if i == 101:
#    break
#  elif i % 2 == 0:
#    #print i
#    sum = sum + i
#print(sum)

numbers  = range(2,101,2)
numbers = list(numbers)
print numbers

evens = [num for num  in numbers
          if num %2 ==0 ]
total = sum(evens)

# evens = []
# for num in numbers:
#   if num %2 ==0
#     evens.append(num)
# total = sum(evens)
 
print total
