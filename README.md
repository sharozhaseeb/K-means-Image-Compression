# K-means-Image-Compression

I have implemented an unsupervised image compression program using K-means clustering. The program is to be given an array of clusters, depending on the values of the clusters respective K-means algorithm is ran and k centroids are calculated on which colors are mapped. <br/>
Reducing the number of different colors reduce the size of the image a lot as the pixels can be mapped as a vector corresponding to a single RGB value rather than all pixels having unique values. <br/>
I have used skimage for image input output & sklearn.cluster for kmeans algorithm.

# To run the program following dependencies should be added;
pip install sklearn <br/>
pip install skimage <br/>
## Make sure the correct path is added where you are placing your image files.

I used cluster values 2,3,5,10,15 and 20 and got the following results. <br/>

#### for k = 2;

#### for k = 3;

#### for k = 5;

#### for k = 10;

#### for k = 15;

#### for k = 20;

#### Original image;
![face](https://user-images.githubusercontent.com/83841336/145388378-7b4d6a27-fbd6-4b75-a5c7-48414777fc82.jpg)
