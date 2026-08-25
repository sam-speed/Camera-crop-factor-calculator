import csv
import os
from datetime import datetime

def save_usage_data(sensor_name, adapter_name, focal_lengh_input, focal_aperture_input, focal_length_result, focal_aperture_result, focal_aperture_equivalent, classification, bouque_ranking):
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists("usage_data.csv")
    fieldnames = ["timestamp", "sensor_name", "adapter_name", "focal_length_input", "focal_aperture_input", "focal_length_result", "focal_aperture_result", "focal_aperture_equivalent", "classification", "bouque_ranking", "new_job_clicked"]

    with open("usage_data.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow({
            "timestamp": timestamp,
            "sensor_name": sensor_name,
            "adapter_name": adapter_name,
            "focal_length_input": focal_lengh_input,
            "focal_aperture_input": focal_aperture_input,
            "focal_length_result": focal_length_result,
            "focal_aperture_result": focal_aperture_result,
            "focal_aperture_equivalent": focal_aperture_equivalent,
            "classification": classification,
            "bouque_ranking": bouque_ranking,
            "new_job_clicked": 0
            })
        return timestamp

def mark_new_job_clicked(timestamp):
    fieldnames = ["timestamp", "sensor_name", "adapter_name", "focal_length_input", "focal_aperture_input", "focal_length_result", "focal_aperture_result", "focal_aperture_equivalent", "classification", "bouque_ranking", "new_job_clicked"]

    with open("usage_data.csv", mode="r", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        if row["timestamp"] == timestamp:
            row["new_job_clicked"] = "1"

    with open("usage_data.csv", mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)