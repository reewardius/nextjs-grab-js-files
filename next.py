import requests
import re
import codecs
from urllib.parse import urlparse

url = "https://opensea.io/_next/static/65b0de93887d723626455ae23569059a4057bdfb/_buildManifest.js"
parsed_url = urlparse(url)
domain = parsed_url.scheme + "://" + parsed_url.netloc

headers = {
    'User-Agent': '1'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    decoded_text = codecs.decode(response.text, 'unicode_escape')
    
    matches = re.finditer(r'static/chunks/[^"]+\.js', decoded_text)
    
    with open('result_combined.txt', 'w') as combined_file:
        for match in matches:
            js_link = f'{domain}/_next/{match.group(0)}'
            print(js_link)
            combined_file.write(js_link + '\n')
            
            map_link = js_link + '.map'
            print(map_link)
            combined_file.write(map_link + '\n')

else:
    print(f"Error {response.status_code}: Unable to retrieve the JS file")
