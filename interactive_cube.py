import turtle
import pyautogui
import numpy as np

# Turtle screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the pen to draw
pen = turtle.Turtle()
pen.hideturtle()

# Define cube vertices and edges
vertices = np.array([
    [-100, -100, -100], [100, -100, -100],
    [100, 100, -100], [-100, 100, -100],
    [-100, -100, 100], [100, -100, 100],
    [100, 100, 100], [-100, 100, 100]
])

edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Back face
    (4, 5), (5, 6), (6, 7), (7, 4),  # Front face
    (0, 4), (1, 5), (2, 6), (3, 7)   # Connecting edges
]

# Numpy perspective projection parameters
def project(point, angle_x, angle_y):
    # Rotation matrices for X and Y axes
    rx = np.array([
        [1, 0, 0],
        [0, np.cos(angle_x), -np.sin(angle_x)],
        [0, np.sin(angle_x), np.cos(angle_x)]
    ])
    ry = np.array([
        [np.cos(angle_y), 0, np.sin(angle_y)],
        [0, 1, 0],
        [-np.sin(angle_y), 0, np.cos(angle_y)]
    ])
    
    rotated = np.dot(rx, point)
    rotated = np.dot(ry, rotated)
    
    # Apply perspective projection (ignore Z-axis)
    return rotated[:2]

# Main loop
angle_x, angle_y = 0, 0

while True:
    # Clear the screen
    pen.clear()

    # Get mouse position with PyAutoGUI
    mouse_x, mouse_y = pyautogui.position()

    # Update angles based on mouse position with Numpy
    angle_x = np.radians((mouse_y - screen.window_height() // 2) / 10)
    angle_y = np.radians((mouse_x - screen.window_width() // 2) / 10)

    # Project and draw cube edges with Turtle
    for edge in edges:
        point1 = project(vertices[edge[0]], angle_x, angle_y)
        point2 = project(vertices[edge[1]], angle_x, angle_y)
        
        pen.penup()
        pen.goto(point1[0], point1[1])
        pen.pendown()
        pen.goto(point2[0], point2[1])

    # Update the screen
    screen.update()

# Copyright (c) 2025 Chase Rainey
# All rights reserved.
# This code is licensed under [MIT License](https://opensource.org/licenses/MIT)