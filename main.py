import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys
import os
import ctypes
# pip install beautifulsoup4  lxml


def google_search(query, num_pages = 9):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    results = []

    for page in range(num_pages):
        search_url = f"https://www.google.com/search?q={query}&start={page * 10}"
        response = requests.get(search_url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            
            for item in soup.select('.tF2Cxc'):
                link = item.select_one('.yuRUbf a')['href'] if item.select_one('.yuRUbf a') else 'No link'
                domain = urlparse(link).netloc if link != 'No link' else 'No domain'
                results.append(domain)
        else:
            print(f"Failed to retrieve search results on page {page + 1}. Status code: {response.status_code}")
            break
    
    return results

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
        print("Script is asking for admin permit......")
        # Yêu cầu quyền admin và khởi động lại script
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()  # Thoát để script mới chạy với quyền admin
run_as_admin()


while(True):

    query = input("Input search (CTRL + C to exit): ")
    search_results = list(set(google_search(query)))
    print("Results search: ")
    # In danh sách
    for i in range(0, len(search_results), 3):
        print(*search_results[i:i+3], sep='           ')  
    # Địa chỉ file cần sửa
    pathToHostsFile = r"C:\Windows\System32\Drivers\etc\hosts"

    try:
        # Đọc nội dung hiện tại của file hosts
        with open(pathToHostsFile, 'r', encoding='utf-8') as file:
            existing_lines = file.readlines()
        # Ghi thêm các domain mới
        with open(pathToHostsFile, 'a', encoding='utf-8') as file:
            for domain in search_results:
                if f"127.0.0.1       {domain}\n" not in existing_lines:
                    file.write(f"127.0.0.1       {domain}\n")
        print(f"\nTHE DATA HAS BEEN LOGGED {pathToHostsFile}.")
        print(f"ALL THE WEBSITE HAS BEEN BLOCKED!!!")
        input("Press Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')
    except PermissionError:
        print("ERROR: No administrator permission!")
    except Exception as e:
        print(f"ERROR: Unknow!")