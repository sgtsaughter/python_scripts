import time
from selenium import webdriver
import requests

send_sms = input("Do you want to send an SMS alert to your cell phone? (y/n)")

if send_sms == 'y':
    phone_number = str(input("Please enter a phone number to be alerted when item is in stock:\n"))
    print(phone_number)
elif send_sms == 'n':
    phone_number = None
else:
    print("Please answer with a 'y' or 'n'")



# For using chrome
browser = webdriver.Chrome('chromedriver')

# Bestbuy PS5 Disk page
# browser.get("https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149")

# Bestbuy purchasable page.  Using to test on a product I know is in stock.
browser.get("https://www.bestbuy.com/site/sony-playstation-pulse-3d-wireless-headset-compatible-for-both-playstation-4-playstation-5-white/6430164.p?skuId=6430164")


buyButton = False

while not buyButton:

    try:
        # If this works then the button is not pytopen
        addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")

        # Button isnt open restart the script
        print({"Playstation OUT OF STOCK"})

        # Refresh page after a one second delay
        time.sleep(1)
        browser.refresh()

    except:

        addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")

        # Click the button and end the script
        print({"Playstation IN STOCK"})
        addToCartBtn.click()
        buyButton = True

        # SMS Alert
        # TODO: textbelt only allows for one text message per day.  Find a new SMS provider.
        if phone_number:
            resp = requests.post('https://textbelt.com/text', {
                'phone': phone_number,
                'message': 'PS5 IN CART!!!',
                'key': 'textbelt',
            })
            print(resp.json())


# SOLD OUT ELEMENT
# <button class="btn btn-disabled btn-lg btn-block add-to-cart-button" disabled="" type="button" data-sku-id="6430161" style="padding:0 8px">Sold Out</button>

# IN STOCK ELEMENT
# <button class="btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button" type="button" data-sku-id="6430164" style="padding:0 8px"><svg aria-hidden="true" role="img" viewBox="0 0 100 100" style="width:16px;height:16px;margin-bottom:-2px;margin-right:9px;fill:currentColor"><use href="/~assets/bby/_img/int/plsvgdef-frontend/svg/cart.svg#cart" xlink:href="/~assets/bby/_img/int/plsvgdef-frontend/svg/cart.svg#cart"></use></svg>Add to Cart</button>
