# K-means-Image-Compression

I have implemented an unsupervised image compression program using K-means clustering. The program is to be given an array of clusters, depending on the values of the clusters respective K-means algorithm is ran and k centroids are calculated on which colors are mapped. <br/>
Reducing the number of different colors reduce the size of the image a lot as the pixels can be mapped as a vector corresponding to a single RGB value rather than all pixels having unique values. <br/>
I have used skimage for image input output & sklearn.cluster for kmeans algorithm.

## To run the program following dependencies have to be installed;
pip install sklearn <br/>
pip install skimage <br/>
## Make sure the correct path is added where you are placing your image files.

I used cluster values 2,3,5,10,15 and 20 and got the following results. <br/>

#### for k = 2; 
![face k=2](https://user-images.githubusercontent.com/83841336/145389208-5179080f-7396-41f5-936e-d38205e6df16.png)
#### for k = 3;
![face k=3](https://user-images.githubusercontent.com/83841336/145389232-87bd0adf-1066-48fe-9e30-dde57447a471.png)
#### for k = 5;
![k=5](https://user-images.githubusercontent.com/83841336/145389234-1d4fe489-a38a-4886-8178-71cfc93a5ebd.png)
#### for k = 10;
![k=10](https://user-images.githubusercontent.com/83841336/145389236-a35d04a5-c107-4ba7-90d6-ab74d1be423c.png)
#### for k = 15;
![k=15](https://user-images.githubusercontent.com/83841336/145389238-2bb32901-2a94-491c-b3c3-0c64a4bd89a3.png)
#### for k = 20;
![k=20](https://user-images.githubusercontent.com/83841336/145389230-39631614-ce52-4fed-85cc-66dd19a792b6.png)
#### Original image;
![face](https://user-images.githubusercontent.com/83841336/145388378-7b4d6a27-fbd6-4b75-a5c7-48414777fc82.jpg)
<br/><br/>
## Observation;
What we can observe is that with k = 2 we have very little information of features; we can only observe eyes and the shape of the face as we move to k= 3; we observe all the features and can predict the gender of the person accurately; then on k=5 we get a cartoony image of the person which is a very popular filter nowadays. At k =10 we get the image which will get as close to original with the least size with all features and smooth edges which gets better at k = 15 where we can observe easily the wave of different centroid on the skin of the person. At k=20 we have a compressed image close to the original with a fraction of the size.
