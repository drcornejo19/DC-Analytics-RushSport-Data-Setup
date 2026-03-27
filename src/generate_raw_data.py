import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)
np.random.seed(42)

N_ROWS = 1000

START_DATE = datetime(2024,1,1)
END_DATE = datetime(2025,6,30)

products = [
("Boca Jersey","Jersey",55000),
("River Jersey","Jersey",56000),
("Argentina Jersey","Jersey",65000),
("Nike Mercurial","Boots",145000),
("Adidas Predator","Boots",160000),
("Puma Future","Boots",138000),
("Training Shorts","Shorts",28000),
("Compression Shorts","Shorts",35000),
("Training Jacket","Training",78000),
("Training Pants","Training",62000),
("Gym Hoodie","Training",85000),
("Football Socks","Accessories",12000),
("Captain Armband","Accessories",10000),
("Sports Backpack","Accessories",26000)
]

sellers=["David","Lucas","Martin"]

channels=["WhatsApp","Instagram","MercadoLibre","Referral"]

status=["Closed","Pending","Cancelled"]

payment_methods=["Transfer","Cash","Credit Card","Debit"]

cities=["CABA","Buenos Aires","Olivos","Vicente Lopez","San Isidro"]

def random_date():
    delta=END_DATE-START_DATE
    days=random.randint(0,delta.days)
    return START_DATE+timedelta(days=days)

rows=[]

for i in range(N_ROWS):

    product=random.choice(products)

    quantity=random.choice([1,1,1,2,2,3])

    price=product[2]

    total=price*quantity

    rows.append({

    "sale_id":1000+i,

    "sale_date":random_date(),

    "customer_name":"Customer_"+str(random.randint(1,350)),

    "customer_city":random.choice(cities),

    "product_name":product[0],

    "product_category":product[1],

    "unit_price":price,

    "quantity":quantity,

    "total_amount":total,

    "seller_name":random.choice(sellers),

    "sales_channel":random.choice(channels),

    "sale_status":random.choice(status),

    "payment_method":random.choice(payment_methods)

    })

df=pd.DataFrame(rows)

Path("data/raw").mkdir(parents=True,exist_ok=True)

df.to_csv("data/raw/sales_raw.csv",index=False)

print("Dataset generado")
print(df.head())
