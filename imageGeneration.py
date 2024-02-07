import cv2 as cv
import numpy as np
import random
import forTurtle

encoding = {
    'left': [ord('l'), ord('e'), ord('f'), ord('t'), ord(' ')],
    'right': [ord('r'), ord('i'), ord('g'), ord('h'), ord('t')],
    'up': [ord('u'), ord('p'), ord(' '), ord(' '), ord(' ')],
    'down': [ord('d'), ord('o'), ord('w'), ord('n'), ord(' ')],
    'stop': [ord('s'), ord('t'), ord('o'), ord('p'), ord(' ')]
}

input_str = input("Enter direction for robot:\n")
trut = forTurtle
turtle_msg = trut.TurtleMsg.msgForTurtle(input_str)

# Split the input string into words and numbers
words = []
numbers = []

for token in input_str.split():
    if token.isalpha():
        words.append(token)
    elif token.isdigit():
        numbers.append(int(token))

for i in range(len(numbers)):
    numbers[i]*=10

# create a black screen of size 800 by 800

rows, cols = len(words), 6 
img = np.zeros((rows*100, 600, 3), np.uint8)

# create horizontal and vertical white lines at 100px apart from each other
for i in range(100, 800, 100):
    cv.line(img, (0, i), (800, i), (255, 255, 255), 1)  
    cv.line(img, (i, 0), (i, 800), (255, 255, 255), 1)  

for i in range(rows):
    word = words[i]
    pattern = encoding[word]
    # print(pattern)
    for j in range(cols-1):
        digit = pattern[j] 
        color_list = [digit,random.randint(1, 250),random.randint(1, 250)]
        color_tuple = tuple(color_list)
        cv.rectangle(img, (j*100, i*100), ((j+1)*100, (i+1)*100), color_tuple, -1)
# set the last recgtangle of every row to ascii value of number in numbers list
for i in range(rows):
    # num_ascii= ord(str(numbers[i]))
    # print(num_ascii)
    cv.rectangle(img, ((cols-1)*100, i*100), ((cols)*100, (i+1)*100), (random.randint(1, 250),random.randint(1, 250),random.randint(1, 250)), -1)


for i in range(rows):
    for j in range(cols):
        print(chr(img[i*100, j*100][0]), end=' ')
    print()

# display the image
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
print(turtle_msg)

class temp:
    def getInstruction(self):
        return turtle_msg