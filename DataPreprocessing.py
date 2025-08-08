import pandas as pd

# Load dataset
input_file = "C:/BigDataAssignment/CombinedData/yellow_tripdata_2015_combined.csv"
df = pd.read_csv(input_file)

# === Step 1: Keep only required columns ===
columns_needed = ['VendorID', 'payment_type', 'trip_distance', 'total_amount']
df = df[columns_needed]

# === Step 2: Clean trip_distance ===
# Remove negative distances and unrealistic outliers (> 800 miles)
df = df[df['trip_distance'].between(0, 800)]

# === Step 3: Clean total_amount ===
# Remove negative or zero total amounts
df = df[df['total_amount'].between(0,2000)]

# === Step 4: Validate VendorID ===
valid_vendor_ids = ["Creative Mobile Technologies", "VeriFone Inc."]
df = df[df['VendorID'].isin(valid_vendor_ids)]

# === Step 5: Validate payment_type ===
valid_payment_types = [
    "Credit card", "Cash", "No charge", "Dispute", "Unknown", "Voided trip"
]
df = df[df['payment_type'].isin(valid_payment_types)]

# === Step 6: Remove any rows with null values (just in case) ===
df.dropna(inplace=True)

# === Output the cleaned dataset ===
output_file = "yellow_tripdata_2015_cleaned.csv"
df.to_csv(output_file, index=False)
print(f"✅ Cleaned dataset saved as {output_file}")