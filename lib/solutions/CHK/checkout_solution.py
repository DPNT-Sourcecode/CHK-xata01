# skus = "EEEBBAAAAAAAAA"
# skus = "EEBAAAEEBA"
# skus = "EEEEBBAAA"
# skus = "FFFFFF"
# skus = "AAAEEB"
skus = "AAAAA"

skus = "B"

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    items = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40,
        "F": 10,
        "G": 20,
        "H": 10,
        "I": 35,
        "J": 60,
        "K": 80,
        "L": 90,
        "M": 15,
        "N": 40,
        "O": 10,
        "P": 50,
        "Q": 30,
        "R": 50,
        "S": 30,
        "T": 20,
        "U": 40,
        "V": 50,
        "W": 20,
        "X": 90,
        "Y": 10,
        "Z": 50
    }

    names = list(items.keys())

    offers = [
        {"name":"AAA", "price": 130, "saving": 20},
        {"name":"AAAAA", "price": 200, "saving": 50},
        {"name":"EEB", "price": 2*items["E"], "saving": items["B"]},
        # {"name":"FFF", "price": 2*items["F"], "saving": items["F"]},
        # {"name":"HHHHH", "price": 45, "saving": 5},
        # {"name":"HHHHHHHHHH", "price": 80, "saving": 20},
        # {"name":"KK", "price": 150, "saving": 10},
        # {"name":"NNNM", "price": 3*items["N"], "saving": items["M"]},
        # {"name":"PPPPP", "price": 200, "saving": 50},
        # {"name":"QQQ", "price": 80, "saving": 10},
        # {"name":"RRRQ", "price": 3*items["R"], "saving": items["Q"]},
        # {"name":"UUUU", "price": 3*items["U"], "saving": items["U"]},
        # {"name":"VV", "price": 90, "saving": 10},
        # {"name":"VVV", "price": 130, "saving": 20},
        ]

    for s in skus:
        if s not in names:
            return(-1)

    for offer in offers:
        offer["items"] = {}
        for i in offer["name"]:
            count = offer["name"].count(i)
            offer["items"][i] = count

    offers_sorted = sorted(offers, key=lambda item: item["saving"], reverse=True)
    basket = {}

    for i in skus:
        count = skus.count(i)
        basket[i] = count

    counter = sum(basket.values())
    total = 0
    offers_used = 0
    offers_used_repeat = -1

    print(basket)

    while counter > 0:
        for offer in offers_sorted:
            keys=(list(offer["items"].keys()))
            check = 0
            temp_basket = dict(basket)
            leave_loop = False
            remaining_items = 0

            print(basket)
            # print(offer)

            for key in keys:
                try:
                    if temp_basket[key] >= offer["items"][key]:
                        temp_basket[key] = temp_basket[key] - offer["items"][key]
                        check += 1

                except:
                    pass

            if check == len(keys):
                print('here')
                total += offer["price"]
                offers_used += 1
                leave_loop = True

            if leave_loop == True:
                print('true')
                continue

        if offers_used_repeat == offers_used:
            for key, value in basket.items():
                total += items[key] * value
            counter = 0
            basket = temp_basket
            print(total)
            return

        offers_used_repeat = offers_used


checkout(skus)
