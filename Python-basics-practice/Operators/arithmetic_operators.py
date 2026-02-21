#1. Take two integers from user and print their sum.

x=int(input())
y=int(input())
print(x+y)

#2. Take two integers and print subtraction result.

print(x-y)

#3. Take two floats and print multiplication result.

print(x*y)

#4. Take two numbers and print division result.

print(x/y)

#5. Take two integers and print floor division result.

print(x//y)

# 6. Take two integers and print remainder using %.

print(x%y)

# 7. Take a number and print its square using **.

print(x**2)

# 8. Take a number and print its cube.

print(x**3)

# 9. Take two numbers and calculate average.

avg=(x+y)/2
print("Average: ",avg)

# 10. Take length and width from user and calculate area.

length=int(input())
width=int(input())

area=length*width

print("Area is: ",area)

# 11. Take radius and calculate area of circle (3.14 * r * r).

r=int(input())

area=3.14*r*r

print("Area is: ",area)

# 12. Take principal, rate, time and calculate simple interest.

principal=int(input())
rate=int(input())
time=int(input())

SI=(principal*rate*time)/100

print("Simple Interest is: ",SI)

# 13. Take total marks of 5 subjects and calculate percentage.

total_marks=int(input())
sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())

total=sub1+sub2+sub3+sub4+sub5
percentage=(total/total_marks)*100

print("Percentage is: ",percentage)

# 14. Take salary and increase it by 10%.

salary=int(input())

increment=salary+(10/100)*salary

print("Increment salary is: ",increment)

# 15. Take a number and divide it by 2 using /= operator.

a=int(input())
a/=2

print(a)

# 16. Take a number and multiply it by 5 using *= operator.

a*=5

print(a)
# 17. Take two numbers and swap them using arithmetic operators.

a=int(input())
b=int(input())

a=a+b
b=a-b
a=a-b

print(a,b)

# 18. Take a number and check if it is even using %.

if a%2==0:
    print("Even")

# 19. Take a number and check if it is odd using %.

if a%2!=0:
    print("Odd")

# 20. Take total seconds and convert into minutes (use // and %).

total_seconds=int(input())

minutes=total_seconds//60

seconds=total_seconds%60

print(f"{minutes} minutes and {seconds} seconds ")

# 21. Take temperature in Celsius and convert to Fahrenheit.

celcius=float(input())

fahrenheit=(celcius*1.8)+32

print(fahrenheit)

# 22. Take two numbers and print their power result.

base=int(input())
component=int(input())

print(base**component)

# 23. Take price and discount %, calculate final price.

price=float(input())
discount=float(input())

final_price=price-((discount/100)*price)

print("Final Price is: ",final_price)

# 24. Take a 3-digit number and find sum of digits using % and //.

num=int(input())

total=0

while num>0:
    digit=num%10
    total+=digit
    num//=10
print(total)

# 25. Take two numbers and print remainder without using % (use formula).

a=int(input())
b=int(input())

q=a//b
rem=a-(b*q)

print(rem)

# 26. Take a number and print half of it.

num=int(input())
print(num//2)

# 27. Take base and height and calculate area of triangle.

base=int(input())
height=int(input())

area=base*height

print(area)

# 28. Take a number and print its square root using ** 0.5.

num=int(input())

print(num**0.5)

# 29. Take monthly salary and calculate yearly salary.

month_salary=int(input())

yearly_salary=month_salary/12

print(yearly_salary)

# 30. Take total bill and number of people, calculate per person share.

total_bill=float(input())
people=int(input())

per_person=total_bill/people

print(per_person)
