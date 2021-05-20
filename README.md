# K-means-Clustering-Using-Mapreduce
In this project we are going to model a simple unsupervised machine learning algorithm k-means clustering using MapReduce for a letter recognition. Although unsupervised algorithm, we will project this problem as a semi-supervised approach by cross-checking test data labels with labels given by clustering models.
We will use publicaly available Letter Recognition Data. This data comprises of 16 features manually engineered from 20000 images of English alphabates(A-Z).

### What is this project?
In this project we are going to create 26 clusters from the given n% training data using k-means clustering algorithm and evaluate the clusters using a classification task by predicting the class labels (alphabates) of the test data. Following is the pictorial representation of entire pipeline:

![image](https://user-images.githubusercontent.com/69912122/118946863-6f533100-b974-11eb-9b5c-76bebccb4d6d.png)

### About Files:
1. sample.py: sample.py will generate training and test data from the given data along with initial 26 cluster centroids. This program takes 'n' as input, where 'n' is the % of data to consider as training data. The execution will output centroids.txt, train.txt, and test.txt in the specified output directory 'Datasets'. User should create the specified output directory 'Datasets' before executing this program.(We will use only the training and centroid data in the k-means clustering algorithm.)
2. Mapper.py: Mapper function will map each data instance to its cluster labels. 
3. reducer.py: The reducer function simply aggregates each data instance cluster membership and finds the updated cluster centroid coordinates.
4. u_reducer: The u_reducer function simply aggregates each data instance cluster membership and finds the updated cluster centroids coordinates with updated labels.
5. model.sh:  This is the shell script. We are designing k-mean clustering algorithm which requires mapper.py and reducer.py to execute I interation and then execute mapper.py and u_reducer.py for I interation. But mapreduce can perform only one iteration, so to avoid manual execution we will write shell script to execute the pipeline. 
6. c_mapper and c_reducer: We will simply use test data to get cluster labels and cluster centroid coordinates.
7. evaluation.py: After execution of this file we will get accuracy(%) and the heatmap of confusion matrix based on the prediction. 


##### Dataset link : https://archive.ics.uci.edu/ml/datasets/Letter+Recognition 
