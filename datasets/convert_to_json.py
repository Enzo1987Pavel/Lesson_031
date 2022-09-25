import csv
import json

CSV_ADS = "ads.csv"
JSON_ADS = "ads.json"
CSV_CATEGORIES = "categories.csv"
JSON_CATEGORIES = "categories.json"


def convert_to_json(csv_file, json_file, model_name):
    result_data = []

    with open(csv_file, encoding="utf-8") as csv_files:
        for row in csv.DictReader(csv_files):
            data_add = {"model": model_name, "pk": int(row["Id"] if "Id" in row else row["id"])}

            if "Id" in row:
                del row["Id"]
            else:
                del row["id"]

            if "is_published" in row:
                if row["is_published"] == "TRUE":
                    row["is_published"] = True
                else:
                    row["is_published"] = False

            if "price" in row:
                row["price"] = int(row["price"])

            data_add["fields"] = row
            result_data.append(data_add)

    with open(json_file, "w", encoding="utf-8") as json_files:
        json_files.write(json.dumps(result_data, ensure_ascii=False))


convert_to_json(CSV_ADS, JSON_ADS, "ads.ad")
convert_to_json(CSV_CATEGORIES, JSON_CATEGORIES, "ads.category")
