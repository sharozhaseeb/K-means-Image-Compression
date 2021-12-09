# K-means-Image-Compression

I have implemented an unsupervised image compression program using K-means clustering. The program is to be given an array of clusters, depending on the values of the clusters respective K-means algorithm is ran and k centroids are calculated on which colors are mapped. 
Reducing the number of different colors reduce the size of the image a lot as the pixels can be mapped as a vector corresponding to a single RGB value rather than all pixels having unique values.
I have used skimage for image input output & sklearn.cluster for kmeans algorithm.

# To run the program following dependencies should be added;
pip install sklearn <br/>
pip install skimage <br/>
## Make sure the correct path is added where you are placing your image files.

