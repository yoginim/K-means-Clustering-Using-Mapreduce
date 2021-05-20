#! /bin/sh

#Prerequisite: 
# Make sure there is no output folder 'Output02' already existing in HDFS

count=1  
while [ $count -lt 16 ] #iteration of 15 times for first map reduce job 
do
  echo "count---------"+"$count" #displays the count number of iteration
  /usr/local/hadoop-3.3.0/bin/hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -mapper "python mapper.py" -reducer "python reducer.py" -input /content/train.txt  -output output1  -file /content/centroids.txt
  /usr/local/hadoop-3.3.0/bin/hadoop fs -get -f /content/output1/part-00000 /content/home/ #copy the output to home folder
  /usr/local/hadoop-3.3.0/bin/hdfs dfs -rm -r /content/output1/  #delete existing output folder
  rm /content/home/centroids.txt #remove any existing copy of centroids.txt
  mv /content/home/part-00000 /content/home/centroids.txt #write the output to 'centroids.txt' file(basically renaming the file)
  count=`expr $count + 1`
done
echo "First Map reduce Done !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! "

#second map reduce job
/usr/local/hadoop-3.3.0/bin/hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -mapper "python mapper.py" -reducer "python u_reducer.py" -input  /content/train.txt  -output output2  -file  /content/home/centroids.txt
/usr/local/hadoop-3.3.0/bin/hadoop fs -get -f /content/output2/part-00000 /content/home/ #copy the output to home folder
/usr/local/hadoop-3.3.0/bin/hdfs dfs -rm -r  /content/output2/  #delete existing output folder
rm /content/home/centroids.txt #remove any existing copy of centroids.txt
mv /content/home/part-00000 /content/home/centroids1.txt #write the output to 'centroids.txt' file

echo "Second Map reduce Done !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! "

#Third map reduce with test data
/usr/local/hadoop-3.3.0/bin/hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -mapper "python c_mapper.py" -reducer "python c_reducer.py" -input /content/test.txt  -output output2  -file /content/home/centroids1.txt
/usr/local/hadoop-3.3.0/bin/hadoop fs -get -f /content/output2/part-00000 /content/home/ #copy the output to home folder
/usr/local/hadoop-3.3.0/bin/hdfs dfs -rm -r /content/output2/  #delete existing output folder
mv /content/home/part-00000 /content/home/predictions.txt #write the output to 'centroids.txt' file

echo "Third Map reduce Done !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! "




