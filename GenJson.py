from duckduckgo_search import DDGS
from urllib.parse import urlparse
import sys
import ctypes
import os
import json

def duckduckgo_search(query, num_results=10):
    with DDGS() as ddgs:
        results = [r["href"] for r in ddgs.text(query, max_results=num_results)]
        domains = {urlparse(url).netloc for url in results}  # Lấy domain và loại bỏ trùng lặp
        return domains

# Địa chỉ file hosts
pathToHostsFile = r"block.json"

while True:
    query = input("Input search (CTRL + C to exit): ").strip()
    if not query:
        print("Query cannot be empty!")
        continue

    search_results = duckduckgo_search(query)

    if not search_results:
        print("No results found.")
        continue

    print("\nResults found:")
    for domain in search_results:
        print(f"- {domain}")

    try:
        # Đọc tệp JSON
        with open(pathToHostsFile, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        # Nếu tệp không tồn tại, khởi tạo cấu trúc mặc định
        data = {"domains": []}
    except json.JSONDecodeError:
        # Nếu tệp bị hỏng, khởi tạo cấu trúc mặc định
        data = {"domains": []}

    # Loại bỏ các tên miền trùng lặp bằng cách sử dụng set
    all_domains = set(data["domains"])  # Tạo một set từ các tên miền hiện tại trong file
    all_domains.update(search_results)  # Thêm các tên miền tìm được từ DuckDuckGo vào set

    # Cập nhật lại danh sách "domains" với các tên miền không trùng lặp
    data["domains"] = list(all_domains)

    # Ghi lại dữ liệu đã cập nhật vào tệp .json
    with open(pathToHostsFile, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Đã thêm các tên miền vào {pathToHostsFile} và loại bỏ trùng lặp.")

    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
