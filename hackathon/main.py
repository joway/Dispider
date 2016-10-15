from hackathon.api import APIService
from hackathon.helper import read_url_file

filename = 'data/url.txt'
links = read_url_file(filename)

for link in links:
    resp = APIService.create_proj(name=link, entry_url=link)
    print(resp)
