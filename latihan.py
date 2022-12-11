from skimage import io, color
img = io.imread('fadli.jpg')
dimensions = color.guess_spatial_dimensions(img)
print (dimensions)
