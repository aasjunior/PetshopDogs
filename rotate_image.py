import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from customtkinter import CTkImage


def rotate_image(image, angle):
    # obter a altura e a largura da imagem
    height, width = image.shape[:2]
    # get the center point of the image
    center = (width / 2, height / 2)
    # get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    # rotate the image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), borderValue=(255, 255, 255))
    # adjust the position of the rotated image
    rotated_center = np.dot(rotation_matrix, [center[0], center[1], 1])
    x_diff = center[0] - rotated_center[0]
    y_diff = center[1] - rotated_center[1]
    translation_matrix = np.float32([[1, 0, x_diff], [0, 1, y_diff]])
    translated_image = cv2.warpAffine(rotated_image, translation_matrix, (width, height), borderValue=(255, 255, 255))
    return translated_image

def select_image(canvas, image_canvas):
    global image_path
    global image
    global rotated_image
    # open a file dialog to select the image
    image_path = filedialog.askopenfilename()
    # load the image
    image = cv2.imread(image_path)
    # rotate the image to the initial position
    rotated_image = rotate_image(image, 0)
    # show the initial image
    show_image(rotated_image, canvas, image_canvas)

def rotate_image_handler(canvas, image_canvas):
    global rotated_image
    angle = 45 # or any other desired angle
    rotated_image = rotate_image(rotated_image, angle)
    show_image(rotated_image, canvas, image_canvas)

def show_image(image, canvas, image_canvas):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image)
    image_tk = CTkImage(image_pil)
    canvas.itemconfigure(image_canvas, image=image_tk)
    canvas.image = image_tk
