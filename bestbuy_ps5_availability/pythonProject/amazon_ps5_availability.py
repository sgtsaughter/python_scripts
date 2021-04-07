import time
from selenium import webdriver
import requests

send_sms = input("Do you want to send an SMS alert to your cell phone? (y/n)")
phone_number = None

while phone_number is None:
    if send_sms.lower() == 'y':
        # TODO: Add phone number validation
        phone_number = str(input("Please enter a phone number to be alerted when item is in stock:\n"))
        print(f"The number {phone_number} will be sent a text message when a ps5 is added to the cart")
    elif send_sms.lower() == 'n':
        phone_number = False
    else:
        print("Please answer with a 'y' or 'n'")
        send_sms = input("Do you want to send an SMS alert to your cell phone? (y/n)")

# For using chrome
browser = webdriver.Chrome('chromedriver')

# Amazon PS5 Disk page
browser.get("https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG?ref_=ast_sto_dp")

# Amazon purchasable page.  Using to test on a product I know is in stock.
# browser.get("https://www.amazon.com/Dust-Off-Disposable-Compressed-Duster-Cans/dp/B00FZYT278/ref=pd_ys_c_rfy_rp_m_231_2?_encoding=UTF8&pd_rd_i=B00FZYT278&pd_rd_r=NS3E483THXB8A9B6KF2R&pd_rd_w=e6Qro&pd_rd_wg=Lhw08&pf_rd_p=5d61ee21-c9c1-4f53-887e-8583c213529a&pf_rd_r=NS3E483THXB8A9B6KF2R&psc=1&refRID=16CZ1HD7B84K5PEQSQRZ")


buyButton = False

while not buyButton:

    try:
        # If this works then the button is not pytopen
        addToCartBtn = addButton = browser.find_element_by_id("outOfStock")

        # Button isnt open restart the script
        print({"Playstation OUT OF STOCK"})

        # Refresh page after a one second delay
        time.sleep(1)
        browser.refresh()

    except:

        addToCartBtn = addButton = browser.find_element_by_id("add-to-cart-button")

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
