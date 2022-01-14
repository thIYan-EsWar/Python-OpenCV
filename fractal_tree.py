import math

import cv2
import numpy as np


class Coordinate(object):
	def __init__(self, x = 0, y = 0):
		self.x, self.y = x, y

	def __call__(self):
		return (self.x, self.y)


def fractal_tree(start, end, length, color = (0, 0, 0), angle = 225):
	if length < 48:
		cv2.circle(canvas, start(), 5, (0.5, 0.25, 1), -1) 
		return

	# Right sub-tree
	angle_left = angle - 25
	x = end.x + math.floor(math.cos(math.radians(angle)) * length)
	y = end.y + math.floor(math.sin(math.radians(angle)) * length)
	fractal_tree(end, Coordinate(x, y), length * decreament_ratio, (0.25, 0.78, 0.36), angle_left)
	
	# left sub-tree
	angle_right = angle + 15
	x = end.x + math.floor(math.cos(math.radians(angle)) * length)
	y = end.y + math.floor(math.sin(math.radians(angle)) * length)
	fractal_tree(end, Coordinate(x, y), length * decreament_ratio, (0.1, 0.6, 0), angle_right)

	# Post-oreder traversal
	cv2.line(canvas, start(), end(), color, 1)

canvas = np.zeros((480, 640, 3))
canvas[:, :] = [220, 235, 204]

draw_tree = False

length = 100
decreament_ratio = 0.9

fractal_tree(Coordinate(550, 430), Coordinate(550, 430), length)
cv2.imshow("Fractal Tree", canvas)

key = cv2.waitKey(10000)
cv2.destroyAllWindows()