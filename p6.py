pos = 5
key = "d"
# oven over skriver du et bogstav ind og ser om commanden kommer igennem,
# fx hvis jeg skriver "r" så vil den sige moved to the right

if key == "r":
    pos + 1
    print("player moved right")
elif key == "l":
    pos -= 1
    print("player moved left")
else:
    print("unknown command")