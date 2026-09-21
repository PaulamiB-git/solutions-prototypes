import cdsapi
import os
import time

client = cdsapi.Client()

# Center of Zurich is approx 47.37, 8.54
zurich_area = [47.5, 8.4, 47.2, 8.7]

output_dir = "../data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Download ONE year at a time to stay under the strict new limits
for year in range(1980, 2024):
    output_filename = f"era5_zurich_hourly_{year}.nc"
    output_path = os.path.join(output_dir, output_filename)

    if os.path.exists(output_path):
        print(f"Year {year} already downloaded. Skipping...")
        continue

    print(f"Requesting hourly data for year {year}...")

    try:
        client.retrieve(
            "reanalysis-era5-single-levels",
            {
                "product_type": "reanalysis",
                "format": "netcdf",
                "variable": "total_precipitation",
                "year": str(year),
                "month": [f"{m:02d}" for m in range(1, 13)],
                "day": [f"{d:02d}" for d in range(1, 32)],
                "time": [f"{h:02d}:00" for h in range(24)],
                "area": zurich_area,
            },
            output_path,
        )
        print(f"Successfully requested/downloaded year {year}")

    except Exception as e:
        print(f"Error downloading year {year}: {e}")
        # Optional: wait a bit before next request to avoid rate limiting
        time.sleep(5)

print("Batch download process finished.")
