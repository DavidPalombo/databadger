import csv
import json

def export_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent = 2, ensure_ascii = False)

def export_csv(data, filename):
    with open(filename, "w", newline = "", encoding = "utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "url",
            "status_code",
            "title",
            "link_count",
            "form_count",
        ])

        writer.writerow([
            data["target"],
            data["pages"][0]["title"],
            data["pages"][0]["status_code"],
            len(data["pages"][0]["links"]),
            len(data["pages"][0]["forms"]),
        ])