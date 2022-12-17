import requests
from bs4 import BeautifulSoup


page = 1
carname = []
carprice = []
while True:
    result = requests.get(
        f"https://www.egy-car.com/last-cars/page/{page}?filters=price.150%2C200%2C250%2C300%2C350%2C400%2C450")
    src = result.content
    soup = BeautifulSoup(src, "html.parser")
    car_name = soup.find_all("h2", {"class": "aps-product-title"})
    car_price = soup.find_all("span", {"class": "carprice"})
    for i in range(len(car_price)):
        carname.append(car_name[i].text)
        carprice.append(car_price[i].text.replace("\n", "").replace("\t", ""))
    if page > 3:
        break
    print(f"page num {page} switched")
    page += 1
print(carname, carprice)


