import requests
import lxml.html

#get the webpage
response = requests.get("http://www.zagat.com/c/new-york-city-ny/sandwich-shop-restaurants")

#parsing
html = lxml.html.fromstring(response.text)
shops = html.xpath('//div[@class="cases"]//div[@class="case js-case"]')
shops_details = html.xpath('//div[@class="cases"]//div[@class="case js-case"]//a/@href')

shop_names = []
for indx,shop in enumerate(shops):
    
    link = shop.xpath('//div[@class="cases"]//div[@class="case js-case"]//a/@href')[indx*2]
    if len(shop.values()) >= 2:
        shop_names.append((shop.values()[1],link))

with open("list_of_sandwhich_shops.csv","w") as f:
    f.write("shop_name,shop_details\n")
    for i in shop_names:
        f.write(i[0]+","+i[1]+"\n")


 

