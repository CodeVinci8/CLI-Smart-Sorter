import json


config_data = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".txt", ".docx", ".pdf", ".xlsx", ".md"],
    "Scripts": [".py", ".json", ".js", ".sh", "bat"]
}

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(config_data, file, indent=4, ensure_ascii=False)