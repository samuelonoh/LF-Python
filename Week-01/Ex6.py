# No of people
types_of_people = 10
x = f"There are {types_of_people} types of people."

#  Those who are binary and don't
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

# Print wat I said
print(f"I said: {x}")
print(f"I also said: '{y}'")

# Joke Evaluation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# concatenation of strings
print(w + e)