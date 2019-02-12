from urllib import request

url1 = open("htmlfile1.html","r+")

headers = {}

#To let know the server accessed by a browser
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

u = request.urlopen("https://www.google.com/")


ustr = u.headers.get_content_charset('utf-8')

print(type(u.read().decode(ustr)))

url1.write(ustr)

url1.close()

