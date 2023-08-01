# Function Definition Practice:
# Define functions according to the following prompts. Run the Replit to verify correct output.


# 1. Function that accepts no arguments. It's called say_hello and returns nothing, just prints 'hello'.

def say_hello():
  print("hello")

say_hello()

# 2. a 'sum' function that accepts two integers and returns the sum.

def sum(x, y):
  return x + y

print(sum(1, 2))

# 3. an 'average' function that accepts two numbers and returns the average.

def average(a, b):
  return sum(a, b) / 2

print(average(25, 50))

# 4. A function that accepts a first name and a last name and formats it to "{last_name}, {first_name}" (returns a string).

def name(first, last):
  return last + ', ' + first

print(name("foo", "bar"))
  
# 5. A function that accepts a first name, last name, graduation year, and student number and returns those four items together in a list.

def student(first, last, grad_year, student_num):
  return [first, last, grad_year, student_num]

print(student("foo", "bar", 1818, 999))

# 6. A function that accepts an integer and returns whether it is above 18 or not (Boolean).

def old_enough(age):
  if age > 18:
    return "adult"
  else:
    return "child"

print(old_enough(50))

#7. A function that accepts a string and prints the string in reverse (no return value).

def rev(string):
  print(string[::-1])

rev("foobar")