import requests
from bs4 import BeautifulSoup

def get_webpage(url):
    """
    Get the HTML content of a webpage.

    Args:
    - url (str): The URL of the webpage.

    Returns:
    - str: The HTML content of the webpage.
    """
    try:
        # Make a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Return the HTML content
            return response.text
        else:
            print(f"Error: Unable to fetch webpage. Status Code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def scrape_webpage(html_content):
    """
    Scrape information from the HTML content of a webpage.

    Args:
    - html_content (str): The HTML content of the webpage.

    Returns:
    - list: A list of scraped information.
    """
    if html_content:
        # Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, 'html.parser')

        # Example: Scraping titles of articles from a hypothetical news website
        article_titles = []

        # Find all elements with a specific class (replace with your target elements)
        title_elements = soup.find_all('h2', class_='article-title')

        # Extract information from the found elements
        for title_element in title_elements:
            article_titles.append(title_element.text.strip())

        return article_titles
    else:
        return None

if __name__ == '__main__':
    # Example usage
    target_url = 'https://example-news-website.com'
    
    # Get the HTML content of the webpage
    webpage_html = get_webpage(target_url)

    if webpage_html:
        # Scrape information from the webpage
        scraped_data = scrape_webpage(webpage_html)

        # Display the scraped data
        if scraped_data:
            print("Scraped Data:")
            for index, data_point in enumerate(scraped_data, start=1):
                print(f"{index}. {data_point}")
        else:
            print("No data scraped.")
