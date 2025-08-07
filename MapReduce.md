
## 📁 Running MapReduce Tasks (Revenue, Payment Type, Distance)

This project uses **Hadoop Streaming** and **Python scripts** to run 3 MapReduce jobs on the NYC Taxi dataset.

### 🚀 Step-by-Step Instructions

---

### 1️⃣ Upload Cleaned CSV to HDFS

```bash
# Create directory
hdfs dfs -mkdir -p /user/hadoop/nyctaxi

# Upload the cleaned CSV
hdfs dfs -put yellow_tripdata_2015_cleaned.csv /user/hadoop/nyctaxi/
```

---

### 2️⃣ Make Python Scripts Executable

```bash
chmod +x unified_mapper.py
chmod +x unified_reducer.py
```

---

### 3️⃣ Run Each MapReduce Task

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

### 4️⃣ View Output Files in HDFS

```bash
hdfs dfs -cat /user/hadoop/output/revenue_by_vendor/part-00000
hdfs dfs -cat /user/hadoop/output/payment_type_freq/part-00000
hdfs dfs -cat /user/hadoop/output/distance_by_vendor/part-00000
```
