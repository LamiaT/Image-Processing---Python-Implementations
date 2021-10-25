"""Filtering via scikit."""

# Importing necessary libraries

import matplotlib.pyplot as plt
from skimage.filters import sobel


# Loading image

original_image = plt.imread("/chocolate_bars.png")


# Detecting edges of objects in images

edge_detected_image = sobel(original_image)


# Function for plot comparison of original and filtered images

def plot_comparison(original_image, filtered_image, filtered_image_title):
    """Compare 2 plots."""
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12, 10), sharex=True, sharey=True)
    ax1.imshow(original_image, cmap=plt.cm.gray)
    ax1.set_title("Original Image")
    ax1.axis("off")
    ax2.imshow(filtered_image, cmap=plt.cm.gray)
    ax2.set_title(filtered_image_title)
    ax2.axis("off")


# Showing plot comparison of original and filtered image

plot_comparison(original_image, edge_detected_image, "Image with Edge Detected")



