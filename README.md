# Block Websites Based on Google Search Results

This Python script automates the process of blocking websites based on Google search results by modifying the system's `hosts` file. It uses the SerpAPI to fetch search results, extracts domain names from the URLs, and then appends these domains to the `hosts` file, effectively blocking them.

## Prerequisites

-   Python 3.x
-   `serpapi` library: Install using `pip install google-search-results`
-   SerpAPI API key: You need a SerpAPI account and API key to use this script. Replace `"d7b14c71aee0bade7ac6c0358c845315c94d27ab53539ea7d39ee1a2d8cf2468"` with your own API key.
-   Administrative privileges: The script modifies the `hosts` file, which requires administrative rights.

## How to Use

1.  **Install Dependencies:**
    ```bash
    pip install google-search-results
    ```
2.  **Replace API Key:**
    -   Open the Python script (`main.py`).
    -   Locate the `api_key` variable in the `get_domains_from_serpapi` function.
    -   Replace the placeholder value with your SerpAPI API key.
3.  **Run the Script:**
    -   Open a command prompt or terminal with administrative privileges.
    -   Navigate to the directory containing the script.
    -   Execute the script using `python main.py`.
4.  **Enter Search Queries:**
    -   The script will prompt you to enter a search query.
    -   Enter your search query and press Enter.
    -   The script will display the extracted domains and append them to the `hosts` file.
    -   The script will print a confirmation message.
    -   Press Enter to continue or Ctrl+C to exit.

## Script Functionality
  
-   **`get_domains_from_serpapi(query, location, hl, gl, google_domain, api_key)`:**
    - Takes a search query and optional parameters (location, language, etc.).
    - Uses SerpAPI to perform a Google search.
    - Extracts domain names from the search result URLs.
    - Returns a list of unique domain names.
    
-   **`is_admin()`:**
    - Checks if the script is running with administrative privileges.
    - Returns `True` if running as admin, `False` otherwise.
-   **`run_as_admin()`:**
    - Requests administrative privileges if the script is not already running as admin.
    - Restarts the script with elevated privileges.
-   **Main Loop:**
    - Prompts the user for a search query.
    - Calls `get_domains_from_serpapi` to get the domains.
    - Prints the extracted domain names.
    - Appends the domains to the `hosts` file (`C:\Windows\System32\Drivers\etc\hosts`).
    - Handles `PermissionError` if the script does not have administrator right.
    - Handles generic Exceptions.
    - Clear the console after each search.

## Important Notes

-   Modifying the `hosts` file can affect your system's network behavior. Use with caution.
-   Ensure you have the necessary permissions to modify the `hosts` file.
-   The script is designed for Windows systems. The `hosts` file path may vary on other operating systems.
-   Always use a valid SerpAPI API key.
-   Be aware of the ethical implications of blocking websites.
-   This script requires admin rights to run, it will ask for admin rights when the script is run.

## Disclaimer

This script is provided as-is, and the user assumes all responsibility for its use. The author is not responsible for any damage or issues caused by this script.