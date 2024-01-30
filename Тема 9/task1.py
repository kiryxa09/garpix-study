import requests
def get_check(url):
  url = requests.get(url)
  return (url.status_code, url.url)


print(get_check("https://google.com"))