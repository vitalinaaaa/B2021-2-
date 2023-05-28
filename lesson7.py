import requests
res_parse_list = []
response = requests.get("https://coinmarketcap.com")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse_list.append(parse_elem_2)
bitcoin_rate = res_parse_list[0]
print(bitcoin_rate)
ethereum_rate = res_parse_list[1]
print(ethereum_rate)
tether_rate = res_parse_list[2]
print(tether_rate)
BNB_rate = res_parse_list[3]
print(BNB_rate)
USD_coin_rate = res_parse_list[4]
print(USD_coin_rate)
XRP_rate = res_parse_list[5]
print(XRP_rate)
Cardano_rate = res_parse_list[6]
print(Cardano_rate)
Dogecoin_rate = res_parse_list[7]
print(Dogecoin_rate)
Polygon_rate = res_parse_list[8]
print(Polygon_rate)
Solana_rate = res_parse_list[9]
print(Solana_rate)

