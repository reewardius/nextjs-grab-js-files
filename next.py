import argparse
import requests
import re
import codecs
from urllib.parse import urlparse

def process_url(url, output_file):
    parsed_url = urlparse(url)
    domain = parsed_url.scheme + "://" + parsed_url.netloc

    headers = {
        'User-Agent': '1'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        decoded_text = codecs.decode(response.text, 'unicode_escape')

        matches = re.finditer(r'static/chunks/[^"]+\.js', decoded_text)

        if output_file:
            with open(output_file, 'w') as combined_file:
                for match in matches:
                    js_link = f'{domain}/_next/{match.group(0)}'
                    combined_file.write(js_link + '\n')
                    map_link = js_link + '.map'
                    combined_file.write(map_link + '\n')
        else:
            for match in matches:
                js_link = f'{domain}/_next/{match.group(0)}'
                print(js_link)
                map_link = js_link + '.map'
                print(map_link)

    else:
        print(f"Error {response.status_code}: Unable to retrieve the JS file")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a URL to extract JavaScript links.')
    parser.add_argument('-u', '--url', type=str, help='URL to process', required=True)
    parser.add_argument('-o', '--output', type=str, help='Output file for results')
    args = parser.parse_args()

    process_url(args.url, args.output)
