# MODULES COMMENTS AND PIP
# Q1 WRITE A PROGRAM TO PRINT TWINKLE,TWINKLE LITTLE STAR POEM
print("""Song Lyrics
Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

Twinkle twinkle little star.
How I wonder what you are.
Up above the world so high.
Like a diamond in the sky.
Twinkle twinkle little star.
How I wonder what you are.

 """) 
# Q2 INSTALL AN EXTERNAL MODULE AND USE IT TO PERFORM AN OPERATION OF YOUR INTEREST
# 01
import turtle
for i in range(36):
    turtle.forward(100)
    turtle.right(170)
turtle.done()

# 02
import pyjokes
print(pyjokes.get_joke())

