# skus = "EEEBBAAAAAAAAA"
# skus = "EEBAAAEEBA"
skus = "EEEEBBAAA"
# skus = "FFFFFF"
# skus = "AAAEEB"
# skus = "AAAAA"

# skus = "B"

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

    offers = {
        "AAA": {"price": 130, "saving": 20},
        "AAAAA": {"price": 200, "saving": 50},
        "EEB": {"price": 2*items["E"], "saving": items["B"]},
        "FFF": {"price": 2*items["F"], "saving": items["F"]},

    }


    for s in skus:
        if s not in names:
            return(-1)

    for name, offer in offers.items():
        offers[name]["items"] = {}
        for n in name:
            count = name.count(n)
            offer["items"][n] = count

    offers_sorted = sorted(offers, key=lambda item: offers[item]["saving"], reverse=True)
    
    print(offers)
    print(offers_sorted)


    basket = {}
    subtotal = 0

    for i in skus:
        count = skus.count(i)
        basket[i] = count

    counter = sum(basket.values())
    total = 0

    while counter != 0:

        valid_offers = []
        attempts = 0

        while attempts == 0:
            for offer in offers_sorted:

                items_in_offer = len(offers[offer]["items"])
                check = 0

                for item, count in offers[offer]["items"].items():

                    try:
                        if offers[offer]["items"][item] <= basket[item]:
                            check += 1
                    except:
                        pass

                    if check == items_in_offer:
                        valid_offers.append(offer)

                
                attempts += 1

        print('=======')
        print(basket)
        print(valid_offers)
        print('=======')

        subtotal += offers[valid_offers[0]]["price"]

        for item, count in offers[valid_offers[0]]["items"].items():
            print(item, count)
            basket[item] = basket[item] - count
        print(subtotal)
        print(basket)
    return





checkout(skus)




