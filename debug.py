I AM SORRY THIS PARTICULAR ONE IS IN A MESS

def mean(numbers):

    total = sum(numbers)
    return total / len(numbers)


# Define a method called student_details that takes in two arguments

def user_details(name, occupation):
    return f"Hi! My name is {name} and I am a {occupation}."



# # # # Call the method
user_name = "Glo"
user_occupation = "Lecturer"


 # 1. Write the error message here:
 #   File "debug.py", line 20, in <module> ((user_occupation))
 # NameError: name 'user_occupation' is not defined

 # 2. Fix the code so that it works.

# Define a method called apple_price which takes in one argument
def apple_price(num_of_apples):
    return num_of_apples * 1.00


###############
# Call the method
# What's wrong with the following code?


# 1. Write down the error message here
#   File "debug.py", line 37, in <module>

# NameError: name 'apple_prices' is not defined

# 2. Fix the code so that it works.


# Define a method called "run" that does not take in any arguments
def run():
    return "This is the method 'run' and it did not take in any arguments!"


# ############################
# # Call the method


def lover_fish(initial_fish):
    num_females = initial_fish * 0.6
    num_males = initial_fish * 0.4
    num_couples = num_males

    # After 3 months, each couple will produce 10 fish in 60:40 ratio
    num_offspring = num_couples * 10

    f_b_fish = num_females + num_offspring * 0.6

    return(f_b_fish)

#


# Step 1: Determine the number of male adults to determine the number of couples

# Number of male adults equals to number of couples
def adult_male_population(initial_fish):
    return initial_fish * 0.4

# Each couple will have 10 babies


def total_babies(n):
    return adult_male_population(n) * 10


# Step 2: Determine the number of adult females and baby females and add them up

def adult_female_population(n):
    return n * 0.6


def total_female(n):
    female_adults = adult_female_population(n)
    female_babies = total_babies(n) * 0.6
    total = female_adults + female_babies
    return total


print(total_female(1600))
print(total_female(100))
