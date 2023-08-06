# Big-data-analytics-in-the-cloud
This repository is created for assignment purpose. Please follow the following sections to reproduce the project, which is to implement the algorithms for computing the descriptive statistics of amount received by each bank using three different approaches. The performance of each approach are to be compared in the report. 

## Get the data source from Kaggle
1. Visit the URL: https://www.kaggle.com/datasets/ealtman2019/ibm-transactions-for-anti-money-laundering-aml?select=HI-Medium_Trans.csv
2. Download HI-Medium_Trans.csv to your local machine
3. Execute "Columns Reduction.py" to get rid of unnecessary columns

## Setup EC2 environment and upload dataset
1. Login to AWS EC2
2. Launch three instances using "SunU-Hadoop-Image v1.4" AMIs, with one master node and two slave nodes
3. Upload HI-Medium_Trans.csv from local machine to master node using WinSCP
4. Connect to the master node and change the directory to where the dataset is located
5. Execute "start-all.sh"
6. Upload dataset to hdfs server using "hadoop fs -put {local path to dataset} {hdfs path for storing dataset}"

## Conventional Approach
1. Create a .py file in master node using "nano {file name}.py"
2. Copy and paste the Python script from "Conventional Approach (Python).py" under Conventional Approach folder to the created Python file
3. Save file and exit nano editor
4. Execute Python file using "python3 {file name}.py"

## MapReduce Approach
1. Create two .py file in master node using "nano {file name}.py" as well, it is recommended to name them as "mapper.py" and "reducer.py" respectively
2. Copy and paste the Python script from "mapper.py" and "reducer.py" under MapReduce Approach folder
3. Change permissions for both .py files using "chmod +x {local path to .py file}"
4. Submit MapReduce job to the hadoop server using "hadoop jar {file path to hadoop-streaming*.jar} -input {hdfs file path to dataset} -output {hdfs file path for storing results} -file {local path to mapper.py} -mapper {local path to mapper.py} -file {local path to reducer.py} -reducer {local path to reducer.py}
5. After the job is done, you can review the output using "hadoop fs -cat {hdfs file path to output file/part-00000}"

## Hive Approach
1. Setup metastore using "schematool -initSchema -dbType derby"
2. Start Hive using "hive" command
3. Execute queries from "HiveQL Queries.txt" under Hive Approach folder one-by-one

## Visualization
1. To visualize the results, execute "Analysis (Visualization).py" on your local machine with any IDE
