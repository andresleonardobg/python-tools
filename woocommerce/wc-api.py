from woocommerce import API
import json
import pandas as pd

'''
get all products and propieties form woocommerce api
'''

wcapi = API(
    url="",
    consumer_key="",
    consumer_secret="",
    version="wc/v3",
    wp_api=True,
)

# data = wcapi.get("products?filter[limit] =-1").json()
data = wcapi.get("products", params={"per_page": 1}).json()[0]


def get_product_ids(start, stop):
    id = []
    name = []
    links = []
    prices = []
    images = []
    for page in range(start, stop):
        response = wcapi.get("products", params={"per_page": 1, "page": page}).json()[0]
        print(f"Page: {page}")
        if response["id"]:
            print(response["id"])
            print(response["name"])
            id.append(response["id"] if response["id"] else "")
            name.append(response["name"] if response["name"] else "")
            links.append(response["permalink"] if response["permalink"] else "")
            prices.append(response["price"] if response["price"] else "")
            images.append(response["images"][0]["src"] if response["images"] else "")

    df = pd.DataFrame(
        {"Producto": name, "link": links, "precio": prices, "imagen": images}
    )
    df.to_csv(f"products_{stop}.csv", index=False)


get_product_ids(start=1, stop=872)
