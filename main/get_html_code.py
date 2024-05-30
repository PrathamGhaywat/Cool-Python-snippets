import requests #pip install requests

def save_html(url, file_path):
    # Send a HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the content of the response
        html_content = response.text

        # Open the file in write mode and write the HTML content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
    else:
        print(f"Unable to get HTML. HTTP response code: {response.status_code}")

# Usage:
url = "http://example.com"
file_path = "output.html"
save_html(url, file_path)
