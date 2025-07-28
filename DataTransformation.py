import pandas as pd
import os

# Input and output paths
input_file = "C:/BigDataAssignment/NYC_TaxiData/yellow_tripdata_2015-01.csv"
output_dir = "C:/BigDataAssignment/processed_chunks/"
os.makedirs(output_dir, exist_ok=True)

# Define chunk size
chunk_size = 500_000

# Mapping dictionaries
vendor_map = {
    1: "Creative Mobile Technologies",
    2: "VeriFone Inc."
}

rate_code_map = {
    1: "Standard rate",
    2: "JFK",
    3: "Newark",
    4: "Nassau or Westchester",
    5: "Negotiated fare",
    6: "Group ride"
}

payment_type_map = {
    1: "Credit card",
    2: "Cash",
    3: "No charge",
    4: "Dispute",
    5: "Unknown",
    6: "Voided trip"
}

# Process in chunks
chunk_no = 0
for chunk in pd.read_csv(input_file, chunksize=chunk_size):
    # Clean and replace values
    if 'VendorID' in chunk.columns:
        chunk['VendorID'] = chunk['VendorID'].map(vendor_map).fillna("Other")

    if 'RatecodeID' in chunk.columns:
        chunk['RatecodeID'] = chunk['RatecodeID'].map(rate_code_map).fillna("Unknown")

    if 'payment_type' in chunk.columns:
        chunk['payment_type'] = chunk['payment_type'].map(payment_type_map).fillna("Unknown")

    # Save processed chunk
    output_path = os.path.join(output_dir, f"processed_chunk_{chunk_no}.csv")
    chunk.to_csv(output_path, index=False)
    print(f"✅ Saved: {output_path}")
    chunk_no += 1
