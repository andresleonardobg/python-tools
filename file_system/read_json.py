import json
import pandas as pd

f = open("products.json", encoding="utf8")

data = json.load(f)

print(len(data["products"]))


def get_products():
    id = []
    name = []
    links = []
    prices = []
    images = []
    sku = []

    for product in data["products"]:
        id.append(product["id"] if product["id"] else "")
        name.append(product["title"] if product["title"] else "")
        links.append(product["permalink"] if product["permalink"] else "")
        prices.append(product["price"] if product["price"] else "sin precio")
        images.append(product["images"][0]["src"] if product["images"] else "")
        sku.append(product["sku"] if product["sku"] else "no tine sku")

    df = pd.DataFrame(
        {
            "sku": sku,
            "Producto": name,
            "link": links,
            "imagen": images,
            "precio": prices,
            "id": id,
        }
    )
    df.to_csv("yeaah_productos.csv", index=False)
    
get_products()
f.close()
