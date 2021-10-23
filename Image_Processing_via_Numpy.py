"""Image Processing via NumPy, Matplotlib."""

# Loading image using Matplotlib
import matplotlib.pyplot as plt

coffee_image = plt.imread("/coffee_original.png")

print(type(coffee_image))
# <class 'numpy.ndarray'>

# Shape of Images
print(coffee_image.shape)
# (264, 376, 3)

# Size of Images
print(coffee_image.size)
# 397056

# Getting separate R,G,B channels of images in grayscale
red_channeled_image = coffee_image[:, :, 0]

green_channeled_image = coffee_image[:, :, 1]

blue_channeled_image = coffee_image[:, :, 2]

plt.imshow(coffee_image, cmap=None)
plt.title("Original Image")
plt.axis("off")
plt.show()

plt.imshow(red_channeled_image, cmap="gray")
plt.title("Red Channeled Image")
plt.axis("off")
plt.show()

plt.imshow(green_channeled_image, cmap="gray")
plt.title("Green Channeled Image")
plt.axis("off")
plt.show()

plt.imshow(blue_channeled_image, cmap="gray")
plt.title("Blue Channeled Image")
plt.axis("off")
plt.show()
