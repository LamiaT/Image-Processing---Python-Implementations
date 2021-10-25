"""Filtering via scikit."""

# Importing necessary libraries

import matplotlib.pyplot as plt
from skimage import exposure


# Loading image

original_image = plt.imread("/chocolate_bars.png")


# Contrast Enhancing using Histogram Equalization of scikit

histogram_equalized_image = exposure.equalize_hist(original_image)


# Contrast Enhancing using Adaptive Histogram Equalization of scikit
adaptive_histeq_image = exposure.equalize_adapthist(original_image, clip_limit=0.05)


# Contrast Enhancing using CLAHE / Contrastive Limited Adaptive Histogram Equalization of scikit
pass


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

plot_comparison(original_image, histogram_equalized_image, "Histogram Equalized Image")
