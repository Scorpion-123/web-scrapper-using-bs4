import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get(
    "https://www.flipkart.com/apple-iphone-12-pro-max-graphite-256-gb/p/itm8dbdf0b986725?pid=MOBFWBYZEF6XQ5ZW&lid=LSTMOBFWBYZEF6XQ5ZWBZ3ZKD&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=820939e3-ff9b-42f7-92f2-3cd7bfa6b0df.MOBFWBYZEF6XQ5ZW.SEARCH&ppt=sp&ppn=sp&ssid=g0ll0197lc0000001605617078376&qH=69776452a026bf07")

items_name = []
prices = []
ratings = []
image_url_new = []

soup = BeautifulSoup(page.content, "html.parser")
item_name = soup.find(attrs={'class': "B_NuCI"}).text
price = soup.find(attrs={"class": "_30jeq3 _16Jk6d"}).text
rating = soup.find(attrs={"class": "_2d4LTz"}).text
image_url = soup.find(attrs={"class": "jMnjzX"}).get("src")

image_url_join = "https:" + str(image_url)

items_name.append(item_name)
prices.append(price)
ratings.append(rating)
image_url_new.append(image_url_join)

data = {"items_name": items_name, "price": prices, "image_url": image_url_new, "ratings": ratings}
# print(data)
print(f"the name of the product is {item_name} the price is {price} and the rating of the product is {rating}")
# The data dictionary of the product
print(data)
