"""Image Processing via scikit image."""

# Loading necessary modules from scikit, matplotlib etc
import matplotlib.pyplot as plt
from skimage import data, color

# Loading images
rocket_image = data.rocket()

# Converting images from colored to gray and vice-versa
gray_scale_image = color.rgb2gray(rocket_image)

rgb_image = color.gray2rgb(gray_scale_image)


# function for visualising images
def show_image(image, title="Image", cmap_type="gray"):
    """Use for visualising images."""
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis("off")
    plt.show()


show_image(rocket_image, "Original Rocket Image")
show_image(gray_scale_image, "Gray Scale Image")







