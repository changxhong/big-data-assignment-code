import pandas as pd
import glob
import os

# Folder containing all your processed CSV chunks
chunk_folder = "C:/BigDataAssignment/processed_chunks/"

# Pattern to match all chunk files
file_pattern = os.path.join(chunk_folder, "processed_chunk_*.csv")

# List all chunk files
chunk_files = sorted(glob.glob(file_pattern))

# Combine all chunks into one DataFrame
combined_df = pd.concat((pd.read_csv(f) for f in chunk_files), ignore_index=True)

# Save the final combined dataset
combined_df.to_csv("C:/BigDataAssignment/CombinedData/yellow_tripdata_2015_combined.csv", index=False)
print("✅ All chunks combined and saved as yellow_tripdata_combined.csv")
