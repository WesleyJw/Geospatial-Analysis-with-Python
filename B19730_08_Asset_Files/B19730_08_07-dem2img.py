"""Convert an ASCII DEM to an image.

First you need to run B19730_08_01-shaded.py
to get the relief.asc input DEM file used here.
"""
import numpy as np

try:
    import Image
    import ImageOps
except:
    from PIL import Image, ImageOps

# Source LIDAR DEM file
source = "relief.asc"

# Output image file
target = "relief.bmp"

# Load the ASCII DEM into a numpy array
arr = np.loadtxt(source, skiprows=6)

# Convert array to numpy image
im = Image.fromarray(arr).convert('RGB')

# Enhance the image:
# equalize and increase contrast
im = ImageOps.equalize(im)
im = ImageOps.autocontrast(im)

# Save the image
im.save(target)
