# Crop image with OpenCV
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This project is an experimental use of OpenCV Library to crop an image. The script will apply Canny on the original image to find the object's edges, and then will crop the biggest area found.

### Requirements
- OpenCV 3+
- Python 2.7+, 3.4+

### Installation
```
git clone git@github.com:SalvoCozzubo/opencv-crop.git
cd opencv-crop
```

### Use
```
python crop.py -i image.jpg --crop
```

Show all commands use ```-h```
```
python crop.py -h
```