# Integers

# number = 109473094638970239870649027738934793865879456746587465868749568947569873685864409859485687094658907498578957879536868685346587368568934857946354580937887643970913984758948810087246547894445689683648564768
# number = -109473094638970239870649027738934793865879456746587465868749568947569873685864409859485687094658907498578957879536868685346587368568934857946354580937887643970913984758948810087246547894445689683648564768
# print(number)

# # INTEGERS RANGE FROM POSITIVE INFINITY TO NEGATIVE INFINITY ONLY LIMITED BY THE SIZE OF YOUR COMPUTER'S MEMORY 

# # BOOLEANS TRUE AND FALSE (LOGICAL DESCRIPTOR FOR MACHINES DECISION MAKING)

# # x = True
# # y = False
# # print(x)
# # print(y)

# # other data types can also be converted to booleans

# number1 = 12
# number2 = 0.00000000000000000000000000000000001
# number3 = -12
# list1 = []
# list2 = [12,23]
# string1 = ""
# string2 = "hello"

# print(bool(number1), bool(number2), bool(number3), bool(list1), bool(list2), bool(string1), bool(string2), sep = "\n")

# light_speed = 3e6

# print(light_speed)
# print(type(light_speed))


# STRINGS

# text = 'This string contains a single quote (') character.' one cannot have the same delimiting quotation outside and also inside a string, they must be different


# text = "This string contains a single quote (') character."
# print(text)

# text = 'This string contains a single quote (") character.'
# print(text)


# print('This string contains a single quote ("\')  character.') # using a back slash suppresses what a character usually means

# print('Ade said and i quote \"this is a delicious meal\" my mum's meals a always the best')

# x = input("Whats is your name ? : ")
# print("My name is " + x)

# print("plan\t\t\t\t\t\t\tlegs") # \t creates a tabulate character in python
# print("plan\n\n\n\n\n\nlegs") # \n creates a newline character in python

# print("List of items: ")
# print("\t1. Bread")
# print("\t2. Eggs")
# print("\t3. beans")
# print("\t4. salad")


# letter = """
# Hello sir,

# Please find attached to this message, the rrequirements the sport as requested.

# The files in the mail are:
#     - CAC docs
#     - SCMUL form
#     - Form 3b

# I will be awaiting next steps from you.

# Regards,
# Secretory.
# """

# print(letter)

# Datatype conversion

# int to str

# x = 10
# str_x = str(x)
# print(type(x))
# print(x)
# print(type(str_x))
# print(str_x)

# print(x*2)
# print(str_x*2)

# type conversion 

# STRING TO INTEGER
# age = input("Please enter your age: ") # all input values in python are interpreted as string types
# print(type(age))

# age_integer = int(age)

# year_of_birth = 2021 - age_integer
# print(year_of_birth)

# NOTE THAT WHEN CONVERTING YOUR VALUE MUST BE A REPRESENTABLE FORMAT OF TARGET DATATYPE

# name = "ade" 
# print(int(name)) # this code will fail because there is no integer representation possible for the word ade

# import datetime # import is used for importing other modules into your project


# print(datetime.datetime.now())

# if 10 < 20: print("hurray") # if key word is used for making decisions

# radius = int(input("Please enter the radius to calculate : "))

# perimeter = 2* (22/7)* radius

# print(perimeter)


a = int(input("Please enter the a : "))
b = int(input("Please enter the b : "))

c = (a**2+b**2)**0.5

print(round(c))