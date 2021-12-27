import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Crop an image from Countour algorithm')
parser.add_argument('--input', '-i', help='Input image', required=True)
parser.add_argument('--show-canny', help='Show Canny algorithm result', action='store_true')
parser.add_argument('--show-result', help='Show image with bounding box before the crop', action='store_true')
parser.add_argument('--output', '-o', help='Output image')
parser.add_argument('--draw-all-areas', help='Draw all areas', action='store_true')
parser.add_argument('--crop', '-c', help='Crop the biggest rectangle found', action='store_true')

args = parser.parse_args()

window_openend = False

# load the target image
image = cv.imread(args.input)

# convert in grayscale
imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# apply Canny for edge
edged = cv.Canny(imageGray, 80, 200)

cannyImage, contours, hierarchy = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

if args.show_canny:
  cv.imshow('img', cannyImage)
  window_openend = True

bestRect = None
area = 0

for c in contours:
  rect = cv.boundingRect(c)
  x,y,w,h = rect

  current_area = w * h
  
  if current_area > area:
    area = current_area
    bestRect = rect
  
  if args.draw_all_areas:
    cv.rectangle(image, (x, y), (x+w, y+h), (0, 120, 255), 2)

x, y, w, h = bestRect

if args.crop:
  imageCropped = image[y:h+y, x:x+w]

  cv.imshow('crop', imageCropped)
  window_openend = True

if not args.draw_all_areas:
  cv.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

if args.show_result:
  cv.imshow('image', image)
  window_openend = True

if not args.output == None:
  cv.imwrite(args.output, image)

# wait for a key press
if window_openend:
  # wait for a key press
  cv.waitKey(0)

  # close all window
  cv.destroyAllWindows()