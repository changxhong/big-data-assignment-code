## 📁 Hadoop MapReduce Implementation – NYC Taxi Data

This section documents the full implementation of three MapReduce jobs using **Hadoop Streaming** and **Python 3 scripts**, run on an **AWS EC2 instance**.

---

## 🧾 Jobs Implemented

| Job Name                   | Mapper Script               | Reducer Script               | Output Directory                         |
| -------------------------- | --------------------------- | ---------------------------- | ---------------------------------------- |
| Total Revenue by Vendor    | `mapper_revenue_vendor.py`  | `reducer_revenue_vendor.py`  | `/user/hadoop/output/revenue_by_vendor`  |
| Frequency of Payment Types | `mapper_freq_payment.py`    | `reducer_freq_payment.py`    | `/user/hadoop/output/payment_type_freq`  |
| Total Distance by Vendor   | `mapper_distance_vendor.py` | `reducer_distance_vendor.py` | `/user/hadoop/output/distance_by_vendor` |

---

## 🗂️ Directory Setup

All files were located under the Hadoop home directory:

```bash
/home/hadoop/
```

---

## 🔧 Mapper and Reducer Scripts

### 🟢 `mapper_revenue_vendor.py`

```python
#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader, None)

for row in reader:
    try:
        vendor = row[0]
        revenue = float(row[3])
        print(f"{vendor}\t{revenue}")
    except:
        continue
```

---

### 🟢 `reducer_revenue_vendor.py`

```python
#!/usr/bin/env python3
import sys

current_vendor = None
total = 0.0

for line in sys.stdin:
    vendor, revenue = line.strip().split('\t')
    revenue = float(revenue)

    if vendor == current_vendor:
        total += revenue
    else:
        if current_vendor:
            print(f"{current_vendor}\t{total:.2f}")
        current_vendor = vendor
        total = revenue

if current_vendor:
    print(f"{current_vendor}\t{total:.2f}")
```

---

### 🟢 `mapper_freq_payment.py`

```python
#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader, None)

for row in reader:
    try:
        payment = row[1]
        print(f"{payment}\t1")
    except:
        continue
```

---

### 🟢 `reducer_freq_payment.py`

```python
#!/usr/bin/env python3
import sys

current_key = None
count = 0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    value = int(value)

    if key == current_key:
        count += value
    else:
        if current_key:
            print(f"{current_key}\t{count}")
        current_key = key
        count = value

if current_key:
    print(f"{current_key}\t{count}")
```

---

### 🟢 `mapper_distance_vendor.py`

```python
#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin)
header = next(reader, None)

for row in reader:
    try:
        vendor = row[0]
        distance = float(row[2])
        print(f"{vendor}\t{distance}")
    except:
        continue
```

---

### 🟢 `reducer_distance_vendor.py`

```python
#!/usr/bin/env python3
import sys

current_key = None
total = 0.0

for line in sys.stdin:
    key, value = line.strip().split('\t')
    value = float(value)

    if key == current_key:
        total += value
    else:
        if current_key:
            print(f"{current_key}\t{total:.2f}")
        current_key = key
        total = value

if current_key:
    print(f"{current_key}\t{total:.2f}")
```

---

## 🏃 Execution Commands

### ✅ Revenue by Vendor

```bash
hdfs dfs -rm -r /user/hadoop/output/revenue_by_vendor

hadoop jar /home/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -input /user/hadoop/nyctaxidata/taxi_2015_cleaned.csv \
  -output /user/hadoop/output/revenue_by_vendor \
  -mapper ./mapper_revenue_vendor.py \
  -reducer ./reducer_revenue_vendor.py \
  -file mapper_revenue_vendor.py \
  -file reducer_revenue_vendor.py
```

---

### ✅ Payment Type Frequency

```bash
hdfs dfs -rm -r /user/hadoop/output/payment_type_freq

hadoop jar /home/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -input /user/hadoop/nyctaxi/taxi_2015_cleaned.csv \
  -output /user/hadoop/output/payment_type_freq \
  -mapper ./mapper_freq_payment.py \
  -reducer ./reducer_freq_payment.py \
  -file mapper_freq_payment.py \
  -file reducer_freq_payment.py
```

---

### ✅ Distance by Vendor

```bash
hdfs dfs -rm -r /user/hadoop/output/distance_by_vendor

hadoop jar /home/hadoop/hadoop-3.3.6/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -input /user/hadoop/nyctaxi/taxi_2015_cleaned.csv \
  -output /user/hadoop/output/distance_by_vendor \
  -mapper ./mapper_distance_vendor.py \
  -reducer ./reducer_distance_vendor.py \
  -file mapper_distance_vendor.py \
  -file reducer_distance_vendor.py
```

---

## 📄 View Results

```bash
hdfs dfs -cat /user/hadoop/output/revenue_by_vendor/part-00000
hdfs dfs -cat /user/hadoop/output/payment_type_freq/part-00000
hdfs dfs -cat /user/hadoop/output/distance_by_vendor/part-00000
```
