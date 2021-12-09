# This is an image compression program implemented through unsupervised Kmeans library in python
# The number of clusters represent the number of colors allowed to represent the image.
# the lower the number of clusters the smaller in size would the resulting image be.

from skimage import io
from sklearn.cluster import KMeans
import numpy as np
import os

print("Done by Sharoz Haseeb")

org = False
clusters =[2,3,5,10,15,20]

# input and rading the image
for cluster in clusters:

    image = io.imread("face.jpg")
    if (not org):
        print("original image")

        org = True
        io.imshow(image)
        io.show()

    print("\n\n","For K = ",cluster, "\n\n")

# Dimensions of the original image
    rows = image.shape[0]
    cols = image.shape[1]

# Flatten the image to a vector
    image = image.reshape(rows*cols,3)

# Implement k-means clustering to form k clusters

    kmeans = KMeans(n_clusters = cluster)
    kmeans.fit(image)
     
# Replacing pixel value with representative centroid
    compressed_image = kmeans.cluster_centers_[kmeans.labels_]
    compressed_image = np.clip(compressed_image.astype("uint8"),0,255)

# Reshape the image to original dimension
    compressed_image = compressed_image.reshape(rows,cols,3)

# Save and display
    os.chdir("") # put your result image path here
    io.imsave("compressed" + str(clusters)+".png",compressed_image)
    io.imshow(compressed_image)
    io.show()
