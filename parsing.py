import requests
from bs4 import BeautifulSoup
import time
import re
import json 

url ='https://www.dns-shop.ru/catalog/markdown/?type=1,2&group=none'
page_number = '&offset='

cookies = {
    'rerf' :'AAAAAF7crgwhOhZRAzZxAg==',
    'ipp_uid' : '1591520780396/f4i2VNui9gD44ZUS/4duY9dJQPd+xduosC9wsQQ==',
    '_csrf' : '8302025d615f797389d3b4a54fe053bf5f1ff61692307702f11943f11d16a0bca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22Bkhgkb2VOa5BQinPS5A8UDcRKpfyeJ6p%22%3B%7D',
    'ipp_uid2' : 'f4i2VNui9gD44ZUS/4duY9dJQPd+xduosC9wsQQ==',
    '_vi' : 'a1118d4efe121b94d48edabdeb83dc37e11c028356d08b109ad6074ea0207684a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22_vi%22%3Bi%3A1%3Bs%3A32%3A%22aace1100578486895a6b5790359238e4%22%3B%7D',
    'PHPSESSID' : '127071c69e4ce9ba6550486cf7f9087b',
    'ipp_uid1' : '1591520780396',
    'cartUserCookieIdent_v3' : '494a7ad6eaae1bc17bef2b405bca096103191bca14d649d1c8d55bd5025989dea%3A2%3A%7Bi%3A0%3Bs%3A22%3A%22cartUserCookieIdent_v3%22%3Bi%3A1%3Bs%3A36%3A%2275dab5cf-410c-374a-83ba-640dea9b8fb0%22%3B%7D',
    '_ym_d' : '1591520785',
    'rrpvid' : '44507363948480',
    'rcuid' : '5d19b4356bfc7d0001afeba4',
    'current_path' : '36a6deaefe233486280d52a15a32eef79187c862e3ebfc4320b201fcb440bc8da%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22current_path%22%3Bi%3A1%3Bs%3A64%3A%22%7B%22city%22%3A%22b464725e-819d-11de-b404-00151716f9f5%22%2C%22method%22%3A%22geoip%22%7D%22%3B%7D',
    '_ym_isad' : '1',
    '_gid' : 'GA1.2.1952433828.1591520785',
    'phonesIdent' : '64959ffeb6edca367cde17a1b15d28d50ab9041a44a9fb1a24faae58f3abccdfa%3A2%3A%7Bi%3A0%3Bs%3A11%3A%22phonesIdent%22%3Bi%3A1%3Bs%3A36%3A%22c2167110-a29f-45c7-b679-e1ee90e415c7%22%3B%7D',
    'city_path' : 'chelyabinsk',
    '_ym_uid' : '1568732876793529228',
    '_ga' : 'GA1.2.1494996371.1591520785',
    '__Secure-APISID' : 'sRO3vdjoJwYuDhGr/AuMWkiRyaxJM_64p3',
    '__Secure-SSID' : 'AbNhjkglO33csRkJa',
    'APISID' : 'sRO3vdjoJwYuDhGr/AuMWkiRyaxJM_64p3',
    '__Secure-HSID' : 'A52-8PHdQXK4VdeKs',
    'SAPISID' : 'sU-VaB1XHkNfGR4c/A8qEL2NnYmLSGyk3A',
    '__Secure-3PSID' : 'xwejR7cdC0EDXTL3boJ3NpDonnbUuBXm5aIPIQZOUYQxUA_DF-FoqwfiTXT77rOJehhnKg.',
    'SID' : 'xwejR7cdC0EDXTL3boJ3NpDonnbUuBXm5aIPIQZOUYQxUA_DeY5uvdcFDaoKAzmmoKrdWA.',
    'HSID' : 'A52-8PHdQXK4VdeKs',
    'SSID' : 'AbNhjkglO33csRkJa',
    'SIDCC' : 'AJi4QfGk011bpXZPltfGrPRSbrnZ-SOWLNJuLrnf-UDhrljYhw5JXhIqg-Oe55Jxh1W9KdaYLJhH',
    '__Secure-3PAPISID': 'sU-VaB1XHkNfGR4c/A8qEL2NnYmLSGyk3A',
    'IDE' : 'AHWqTUnNOqkN_67H34KmvPsDfKbynNpF7veajfX_3Ntc7bmkx-LX2kdqXNJGdIXJ',
    '1P_JAR': '2020-6-7-8',
    'NID': '204=cGkzQgsDj908fmAumKeKQcASbUM0zPFdo-tRG8U9ZRhcWAh5OHPzgJswMCzbrwgCVHy3CphRuS5DhqQCzFED18n3UZIhpw_VbWJH0WBVbwqr2PyEg7OahTL55OTN96G45LWeySAHtLqYf5OFrVaI28VQ1Nc0UrfYNl1CQdJhJ35XcuhfAHPB1_f5iln1TJZr3tOH8GY5AvNJdBv0IhhNuOl2WQXU2u_9z-Vh-ANJe2m0w7Cnr6lILqZ0JJYDM-SUy11xlVLo3Ade_VRFs0thuuKkOnkyI3km',
    'SEARCH_SAMESITE' : 'CgQI0Y8B',
    'CONSENT' : 'YES+RU.ru+20170312-18-0'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

html_code = requests.get(url, cookies = cookies, headers = headers)
soup = BeautifulSoup(html_code.text, 'lxml')

product_count = soup.find('span', class_= 'count-products').text
counts = re.findall('(\d+)', product_count)
count = int(counts[0]) // 20

json_product = {}
j = 0

for k in range(count + 1):
    new_url = url + page_number + str(20 * k)
    html_code = requests.get(new_url, cookies = cookies, headers = headers)
    soup = BeautifulSoup(html_code.text, 'lxml')

    products = soup.find_all('div', class_ = 'product')

    for div in products:
            
    title = div.find('a', class_='ec-price-item-link').text

        price = div.find('div', class_ = 'price_g')
        new_price = price.find('span').text

        tovar = {
            'title' : title,
            'price' : new_price
        }

        json_product[j] = tovar   #making a JSON with all info
       j += 1

part = len(json_product)

with open('parser/sneakers_list.json','a') as file:   #write info into JSON file
    json.dump(json_product, file) 
print('Parsing is done. File is ready to post')
time.sleep(36000)