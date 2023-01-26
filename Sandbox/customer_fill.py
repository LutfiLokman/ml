import json

pasted_text = """
Sila sertakan

Nama: Nashihin Hanis binti Ismail
Alamat: 2D, Central Residence, Lorong Tun Ahmad Zaidi Adruce 46F, 96000 Sibu, Sarawak
Telefon: +60126316343
Email: nashihinhanis@gmail.com

===
Item:
1. Zip card case in Gold/Light Khaki Chalk
2. Dzikir Bus
3. Lanyard
===

Total: Rm 190 + rm 210
Shipping: 10sm/15ss(postage)

Deposit(RM): 125

ETA End of Dec

Thank you for shopping with us!
"""

item_data = pasted_text.split("===")
item_data = [i for i in item_data if "Item" in i]
item_data = item_data[0].split(":")[1].strip()

item_list = "".join(
    k
    for k in item_data
    if k not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
)
item_list = item_list.split("\n")

price_text = "Rm 190 + rm 210 +rm 20"
price_text = price_text.split("+")
price_list = [float("".join(x for x in i if x in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."])) for i in
              price_text]

total_price = sum(price_list)

cost_list = [1, 2, 3]
column_list = ["product", "price", "cost"]

items_tuple = tuple(zip(item_list, price_list, cost_list))

res = [{"product": sub[0], "price": sub[1], "cost": sub[2]} for sub in items_tuple]
