cd $HADOOP_PREFIX

bin/hadoop fs -rm -f -R input_data
bin/hadoop fs -rm -f -R means result

bin/hadoop fs -mkdir input_data
bin/hadoop fs -put /scripts/star2002-sample.csv /input_data

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
    -input input_data \
    -output means \
    -mapper "python mapper1.py" \
    -reducer "python reducer1.py" \
    -file /scripts/mapper1.py \
    -file /scripts/reducer1.py
bin/hadoop fs -cat means/part-* > /scripts/means.txt

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar \
	-input input_data \
	-output result \
	-mapper "python mapper2.py" \
	-reducer "python reducer2.py" \
	-file /scripts/mapper2.py \
	-file /scripts/reducer2.py \
	-file /scripts/means.txt

bin/hadoop fs -cat result/part-* > /scripts/results.txt
