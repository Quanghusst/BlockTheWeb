from serpapi import GoogleSearch
from urllib.parse import urlparse
import os
import json

def get_domains_from_serpapi(query, location="Hanoi, Vietnam", hl="vi", gl="vn", google_domain="google.com.vn", api_key="d7b14c71aee0bade7ac6c0358c845315c94d27ab53539ea7d39ee1a2d8cf2468"):
    """
    Tìm kiếm Google bằng SerpAPI và trả về danh sách các domain.
    """
    params = {
        "q": query,
        "location": location,
        "hl": hl,
        "gl": gl,
        "google_domain": google_domain,
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    domains = []
    if "organic_results" in results:
        for item in results["organic_results"]:
            if "link" in item:
                link = item["link"]
                domain = urlparse(link).netloc
                domains.append(domain)
    return domains

# Địa chỉ file hosts
pathToHostsFile = "block.json"  # Removed the 'r' prefix as it's not needed for relative paths

while True:
    try:
        query = input("Input search (CTRL + C to exit): ").strip()
        if not query:
            print("Query cannot be empty!")
            continue

        search_results = get_domains_from_serpapi(query)

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

    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')