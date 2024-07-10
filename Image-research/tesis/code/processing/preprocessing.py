from PIL import Image
import cv2


def rgb_to_hsv(img):
  return cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

def rgb_to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)