#age = 34
#age_as_str = str(age)
#print("you are " + age_as_str)
#print(f"you are {age}")

#name = "Jose"
#greeting = f"how are you, {name}?"
#print(greeting)
#f"" = f string#

#name = "Bob"
#print(greeting)

name = "Jose"
final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)

name = "Jose"
final_greeting = "how are you, {name}?"
jose_greeting = final_greeting.format(name=name)
print(jose_greeting)