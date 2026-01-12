#Our First graphical user interface(GUI)

#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. 
# This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def display_image(picture):
    for row in picture:     # iterate through each row
        line = ""           # create an empty line of text
        for pixel in row:   # iterate through each "pixel/space" in the row and replace
            if pixel == 0:
                line += " "  # 0-> spaces
            else:
                line += "*"  # 1-> *
        print(line)         # print each row

display_image(picture)

#Explanation: Picture is a 2D list, where each inner list is a row and each number is a pixel.
# The function iterates through the picture row by row.
# For each row, it creates an empty string and iterates through each number:
# converting 0s to spaces and 1s to asterisks to construct the row.
# Once the row is complete, it prints the string and repeats the process with the next row,
#  until the entire image is displayed on the screen.