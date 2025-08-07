## 📁 Running MapReduce Tasks (Revenue, Payment Type, Distance)
This project uses **Hadoop Streaming** and **Python scripts** to run 3 MapReduce jobs on the NYC Taxi dataset.

## ⚙️ Hadoop Setup Requirements

- Hadoop installed and configured on an EC2 instance
- Java installed
- HDFS and YARN running:
  ```bash
  start-dfs.sh
  start-yarn.sh
````

---

## 📁 Folder Structure

```
nyctaxi_project/
└── mapreduce_jobs/
    ├── unified_mapper.py
    ├── unified_reducer.py
    └── yellow_tripdata_cleaned.csv
```

---
## 1️⃣ Setup

1. **Navigate to project folder**

   ```bash
   cd /home/hadoop/nyctaxi_project/mapreduce_jobs
   ```

2. **Download the dataset**

   ```bash
   wget "https://www.dropbox.com/s/your_file_id/yellow_tripdata_cleaned.csv?dl=1" -O yellow_tripdata_cleaned.csv
   ```

3. **Upload dataset to HDFS**

   ```bash
   hdfs dfs -mkdir -p /user/hadoop/nyctaxi
   hdfs dfs -put yellow_tripdata_cleaned.csv /user/hadoop/nyctaxi/
   ```

4. **Create mapper and reducer**

   * `unified_mapper.py`: handles "revenue", "distance", and "payment"
   * `unified_reducer.py`: aggregates totals or frequencies

5. **Make Python scripts executable**

   ```bash
   chmod +x unified_mapper.py unified_reducer.py
   ```

### 2️⃣ Run Each MapReduce Task

---

#### ➤ Total Revenue by Vendor

```bash
hdfs dfs -rm -r /user/hadoop/output/revenue_by_vendor

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
  -input /user/hadoop/nyctaxi/yellow_tripdata_2015_cleaned.csv \
  -output /user/hadoop/output/revenue_by_vendor \
  -mapper "./unified_mapper.py revenue" \
  -reducer "./unified_reducer.py revenue" \
  -file unified_mapper.py \
  -file unified_reducer.py
```

---

#### ➤ Frequency of Payment Type

```bash
hdfs dfs -rm -r /user/hadoop/output/payment_type_freq

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
  -input /user/hadoop/nyctaxi/yellow_tripdata_2015_cleaned.csv \
  -output /user/hadoop/output/payment_type_freq \
  -mapper "./unified_mapper.py payment" \
  -reducer "./unified_reducer.py payment" \
  -file unified_mapper.py \
  -file unified_reducer.py
```

---

#### ➤ Total Distance by Vendor

```bash
hdfs dfs -rm -r /user/hadoop/output/distance_by_vendor

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
  -input /user/hadoop/nyctaxi/yellow_tripdata_2015_cleaned.csv \
  -output /user/hadoop/output/distance_by_vendor \
  -mapper "./unified_mapper.py distance" \
  -reducer "./unified_reducer.py distance" \
  -file unified_mapper.py \
  -file unified_reducer.py
```

---

### 3️⃣ View Output Files in HDFS

```bash
hdfs dfs -cat /user/hadoop/output/revenue_by_vendor/part-00000
hdfs dfs -cat /user/hadoop/output/payment_type_freq/part-00000
hdfs dfs -cat /user/hadoop/output/distance_by_vendor/part-00000
```
