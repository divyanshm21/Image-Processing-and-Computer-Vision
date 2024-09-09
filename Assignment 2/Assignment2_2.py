import cv2 as cv
import numpy as np

def solve(num, image):
    radius = 25
    dot_space = 10
    x = 50
    y = 50
    matrix = np.array([
        [[1, 1, 1], [1, 0, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 0], [1, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        [[1, 0, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [0, 0, 1]],
        [[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1]],
    ])
    for i, number in enumerate(num):
        number = int(number)
        for row in range(5):
            for col, dot in enumerate(matrix[number][row]):
                x_coor = i * (250) + col * (53) + x
                y_coor = row * (53) + y
                if dot == 1:
                    cv.circle(image, (x_coor, y_coor),
                              25, (255),
                              thickness=cv.FILLED)


num = str(input())
num = num[-2:]
img = np.zeros((300, 500), dtype='uint8')
solve(num, img)
cv.imshow('display', img)
cv.waitKey(0)
