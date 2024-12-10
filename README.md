# SempreMilan Headlines Scraper

## Description
This Python script scrapes the latest headlines from the SempreMilan website (https://sempremilan.com) using the Beautiful Soup library.
It sends a request to the website, retrieves the HTML content, and extracts all headlines.

## Requirements
- Python 3.x
- requests library
- beautifulsoup4 library

You can install the required libraries using pip:

'''bash
pip install requests beautifulsoup4
'''

## How to Use
1. Clone the repository to your local machine:

   '''bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   '''

2. Run the Python script:

   '''bash
   python scraper.py
   '''

3. The script will output the latest headlines from the SempreMilan website.

## Code Explanation
- **Imports**: The script uses the "requests" library to make HTTP requests and "BeautifulSoup" from the "bs4" module to parse HTML content.
- **URL**: The URL of the SempreMilan website is defined, and a GET request is sent to retrieve the page.
- **Response Handling**: If the response status code is 200 (OK), the script proceeds to parse the content.
- **Headline Extraction**: The script finds all headlines tags and prints the text of each headline in a formatted output.
- **Error Handling**: If the request fails, it prints an error message with the status code.

## Example Output
'''
- Headline 1: AC Milan Secure Victory Against Rivals
- Headline 2: Transfer News: Rumors Surrounding Key Players
- Headline 3: Match Analysis: Key Moments from Last Night's Game
'''

## Contributions
Feel free to fork this repository and make enhancements! If you encounter any issues, please open an issue in the repository.

