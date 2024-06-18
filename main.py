import requests
from bs4 import BeautifulSoup
import smtplib

YOUR_EMAIL = "YOUR EMAIL ADDRESS"
YOUR_PASSWORD = "YOUR PASSWORD"

SMTP_ADDRESS = "smtp.gmail.com"


BUY_PRICE = 200
URl = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

Headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

response = requests.get(url=URl, headers= Headers)
data = response.text
soup = BeautifulSoup(data, "lxml")


price = soup.find(name="span", class_="a-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
# print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)



if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URl}".encode("utf-8")
        )


