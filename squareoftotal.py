total_sum = 0 

for numbers in range(1, 11):
   if numbers / 4 == 1: 
     for i in range(5):
     
       numbers = numbers *  4 
       multiples = round(numbers /4)
       total_sum += multiples 
       print(multiples) 
print("total sum of multiples is ", total_sum)
total_sum2 = 0        
for numbers in range(1, 11):
   if numbers / 8 == 1: 
     for i in range(5):
     
       numbers = numbers *  8 
       multiples = round(numbers /8) 
       total_sum2 += multiples 
       print(multiples)
print("total sum of multiples is ", total_sum2)
print("sum of multiples 4 and 8 is ", total_sum + total_sum2)
print("square of total sum is ", (total_sum + total_sum2) * (total_sum + total_sum2))
