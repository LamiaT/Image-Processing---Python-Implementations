"""Thresholding Algorithms for Image Processing."""

# Importing necessary libraries
import matplotlib.pyplot as plt

# Loading grayscale image
original_grayscale_image = plt.imread("/coffee_beans_grayscale.png")

# Binary Thresholding:::

# Setting optimal threshold value
threshold = 127

# Applying thresholding to image to make it binary
binary_image = original_grayscale_image > threshold

# Inverted Thresholding:::

# Applying thresholding to image to make it inverted binary
inverted_binary_image = original_grayscale_image <= threshold

# Histogram-based / Global Thresholding::: Used for uniform lighted bg
from skimage.filters import threshold_otsu

global_threshold = threshold_otsu(original_grayscale_image)

global_binary_image = original_grayscale_image > global_threshold

# Adaptive-based / Local Thresholding::: Used for uneven lighted bg
from skimage.filters import threshold_local

block_size = 37 # ODD NUMBER

local_threshold = threshold_local(original_grayscale_image, block_size, offset=10)

local_binary_image = original_grayscale_image > local_threshold


# function for visualising images
def show_image(image, title="Image", cmap_type="gray"):
    """Use for visualising images."""
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis("off")
    plt.show()


# Visualizing the original grayscale image and its binary, inverted_binary images
show_image(original_grayscale_image, "Original Grayscale Image")

show_image(binary_image, "Thresholded Binary Image")

show_image(inverted_binary_image, "Thresholded Inverted Binary Image")

show_image(global_binary_image, "Thresholded Global Binary Image")

show_image(local_binary_image, "Thresholded Local Binary Image")

