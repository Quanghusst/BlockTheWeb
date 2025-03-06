from duckduckgo_search import DDGS
from urllib.parse import urlparse
import sys
import ctypes
import os

def duckduckgo_search(query, num_results=10):
    with DDGS() as ddgs:
        results = [r["href"] for r in ddgs.text(query, max_results=num_results)]
        domains = {urlparse(url).netloc for url in results}  # Lấy domain và loại bỏ trùng lặp
        return domains

def is_admin():
    """
    Kiểm tra xem script có đang chạy với quyền admin không.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    """
    Yêu cầu quyền admin và khởi động lại script nếu cần.
    """
    if not is_admin():
        print("Script is asking for admin permission...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()


run_as_admin()

# Địa chỉ file hosts
pathToHostsFile = r"C:\Windows\System32\Drivers\etc\hosts"

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
        # Đọc nội dung hiện tại của file hosts
        with open(pathToHostsFile, 'r', encoding='utf-8') as file:
            existing_lines = file.readlines()

        # Ghi thêm các domain mới
        with open(pathToHostsFile, 'a', encoding='utf-8') as file:
            for domain in search_results:
                entry = f"127.0.0.1       {domain}\n"
                if not any(domain in line for line in existing_lines):
                    file.write(entry)

        print(f"\nThe data has been logged in {pathToHostsFile}.")
        print("All websites have been blocked!")

        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

    except PermissionError:
        print("ERROR: No administrator permission!")
    except Exception as e:
        print(f"ERROR: {e}")
