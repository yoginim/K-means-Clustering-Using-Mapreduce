#! /bin/sh

#Prerequisite: 
# Make sure there is no output folder 'Output02' already existing in HDFS

count=1  
while [ $count -lt 16 ] #iteration of 15 times for first map reduce job 
do
  echo "count---------"+"$count" #displays the count number of iteration
  hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -mapper "python3 /home/amghosh/CC_02/mapper.py" -reducer "python3 /home/amghosh/CC_02/reducer.py" -input /user/amghosh/InputTrain -output /user/amghosh/Output02  -file /home/amghosh/CC_02/centroids.txt
  hadoop fs -get -f /user/amghosh/Output02/part-00000 /home/amghosh/CC_02/ #copy the output to home folder
  hdfs dfs -rm -r /user/amghosh/Output02  #delete existing output folder
  rm /home/amghosh/CC_02/centroids.txt #remove any existing copy of centroids.txt
  mv /home/amghosh/CC_02/part-00000 /home/amghosh/CC_02/centroids.txt #write the output to 'centroids.txt' file(basically renaming the file)
  ((count++))
done
echo "First Map reduce Done !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! "

#second map reduce job
hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -mapper "python3 /home/amghosh/CC_02/mapper.py" -reducer "python3 /home/amghosh/CC_02/u_reducer.py" -input /user/amghosh/InputTrain -output /user/amghosh/Output02  -file /home/amghosh/CC_02/centroids.txt
hadoop fs -get -f /user/amghosh/Output02/part-00000 /home/amghosh/CC_02/ #copy the output to home folder
hdfs dfs -rm -r /user/amghosh/Output02  #delete existing output folder
rm /home/amghosh/CC_02/centroids.txt #remove any existing copy of centroids.txt
mv /home/amghosh/CC_02/part-00000 /home/amghosh/CC_02/centroids.txt #write the output to 'centroids.txt' file

echo "Second Map reduce Done !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! "

Third map reduce with test data
hadoop jar /usr/local/hadoop-3.3.0/share/hadoop/tools/lib/hadoop-streaming-3.3.0.jar -mapper "python3 /home/amghosh/CC_02/c_mapper.py" -reducer "python3 /home/amghosh/CC_02/c_reducer.py" -input /user/amghosh/InputTest -output /user/amghosh/Output02  -file /home/amghosh/CC_02/centroids.txt
hadoop fs -get -f /user/amghosh/Output02/part-00000 /home/amghosh/CC_02/ #copy the output to home folder
hdfs dfs -rm -r /user/amghosh/Output02  #delete existing output folder
mv /home/amghosh/CC_02/part-00000 /home/amghosh/CC_02/predictions.txt #write the output to 'centroids.txt' file

echo "Third Map reduce Done !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! "

python3 /home/amghosh/CC_02/evaluation.py



