x = 2
print(x)


my_first_list = ['apple', 1, 'banana', 2]
my_fruit_list = ['apple', 'banana']
my_int_list = [1,2,3]

print(my_first_list[2])
print(my_int_list[0])

cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}
print(cal_lookup['apple'])
cal_lookup['orange']

for f in my_fruit_list:
	print(f)


for f in my_fruit_list:
	pass
print(f)


def sq_int(x):
	y = x**2
	return y

print(sq_int(9))
print(sq_int(4))

#Excercises
#Write a while Loop

x = 12
while x < 20:
  print(x)
  x += 1

  #Write a loop that loop over the keys in a dictionary and prints the values

  state_capitals = {'alabama': 'montegomery', 'alaska': 'juneau', 'arkansas': 'little rock'}

  for state in state_capitals:
    print(state_capitals[state])

#Write the functions is_odd and is_even that are shown in the lecture

def is_even(x):
    if x % 2 == 0:
        return True
    else: 
        return False

is_even(5)


def is_odd(x):
    if x % 2 != 0:
        return True
    else: 
        return False

is_odd(999)

# Loop over my_first_list and square the value if the value is a number, 
# and print the calories of the fruit if it’s a fruit 
# (hint: use the dictionary to look up the calories)



for f in my_first_list:
    # print(f)
    # print(isinstance(f, int))
    if isinstance(f, int):
        print(f*f)
    else:
        print(str(cal_lookup[f]) + " calories")

###
# Write a function
# - Takes a dictionary as an argument
# - Loops over the keys in the dictionary
# - Prints the square of the value in the value
# - Hint: use the `cal_lookup` dictionary for testing.


def value_squared(dictionary):

    for value in dictionary:
        x = dictionary[value]
        print(x*x)

value_squared(cal_lookup)





       
        