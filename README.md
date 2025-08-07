# big-data-assignment-code

# NYC Taxi Data Processing with Python

This project processes the **NYC Yellow Taxi Trip dataset** by replacing coded values in key columns with human-readable descriptions. It is designed to handle large CSV files (12+ million rows) using Python, and outputs a cleaned dataset suitable for analysis or visualization.

---

## 📁 Dataset

- **Source**: https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data
- **File Used**: `yellow_tripdata_2025-01.csv`
- **Size**: ~1.85 GB
- **Total Records**: ~12.7 million

---

## 🔍 Description of Fields Processed

The script replaces numeric codes in the following columns:

### ✅ VendorID
| Code | Description                   |
|------|-------------------------------|
| 1    | Creative Mobile Technologies  |
| 2    | VeriFone Inc.                 |

### ✅ RatecodeID
| Code | Description                   |
|------|-------------------------------|
| 1    | Standard rate                 |
| 2    | JFK                           |
| 3    | Newark                        |
| 4    | Nassau or Westchester         |
| 5    | Negotiated fare               |
| 6    | Group ride                    |

### ✅ payment_type
| Code | Description                   |
|------|-------------------------------|
| 1    | Credit card                   |
| 2    | Cash                          |
| 3    | No charge                     |
| 4    | Dispute                       |
| 5    | Unknown                       |
| 6    | Voided trip                   |

