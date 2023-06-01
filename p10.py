#pos = 5

#def move():
    #global pos
    #pos += 1
    #move ()

#def move(by_amount):
    #global pos
    #normalt ikke det bedste at bruge global amount
    #pos += by_amount
#move (5)

def move(pos, by_amount):
    new_pos = pos + by_amount
    return new_pos
final_pos = move(0, 5)

print(final_pos)
