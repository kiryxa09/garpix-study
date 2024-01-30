def insert_params(url, *args):
  for arg in args:
    url = url.replace("@", arg, 1)
  return url

print(insert_params('https://www.ozon.ru/search/?from_global=@&sorting=@&text=@', "true", "price", "d3"))