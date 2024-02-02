import requests
from bs4 import BeautifulSoup

# The url of the target web
url = 'https://openai.com/careers/distributed-systemsml-engineer'
# Send the request
response = requests.get(url)
jd_text=[]
# Check if it's successful
if response.status_code == 200:
    # Parse the content
    soup = BeautifulSoup(response.text, 'html.parser')
    # Check the 'p' tag
    paragraphs = soup.find_all('p')
    #print(paragraphs)
    # Get the text
    jd_text=''
    for p in paragraphs:
      jd_text=jd_text+p.get_text()
      #jd_text.append(p.get_text())
    print(jd_text)
else:
    print('Failed to retrieve the webpage')