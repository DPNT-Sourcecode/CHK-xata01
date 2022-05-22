skus = "EEEBBAAAAAAAAA"

# skus = "EE"

# skus = "FFFFFF"

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

    # offers = {
    #     "AAA": {"price": 130, "saving": 20},
    #     "AAAAA": {"price": 200, "saving": 50},
    #     "EEB": {"price": 2*items["E"], "saving": items["B"]},
    #     "FFF": {"price": 2*items["F"], "saving": items["F"]},
    #     "HHHHH": {"price": 45, "saving": 5},
    #     "HHHHHHHHHH": {"price": 80, "saving": 20},
    #     "KK": {"price": 150, "saving": 10},
    #     "NNNM": {"price": 3*items["N"], "saving": items["M"]},
    #     "PPPPP": {"price": 200, "saving": 50},
    #     "QQQ": {"price": 80, "saving": 10},
    #     "RRRQ": {"price": 3*items["R"], "saving": items["Q"]},
    #     "UUUU": {"price": 3*items["U"], "saving": items["U"]},
    #     "VV": {"price": 90, "saving": 10},
    #     "VVV": {"price": 130, "saving": 20},
    # }
    # offers = [
    #     {"offer":"AAA", "price": 130, "saving": 20},
    #     {"offer":"AAAAA", "price": 200, "saving": 50},
    #     {"offer":"EEB", "price": 2*items["E"], "saving": items["B"]},
    #     {"offer":"FFF", "price": 2*items["F"], "saving": items["F"]},
    #     {"offer":"HHHHH", "price": 45, "saving": 5},
    #     {"offer":"HHHHHHHHHH", "price": 80, "saving": 20},
    #     {"offer":"KK", "price": 150, "saving": 10},
    #     {"offer":"NNNM", "price": 3*items["N"], "saving": items["M"]},
    #     {"offer":"PPPPP", "price": 200, "saving": 50},
    #     {"offer":"QQQ", "price": 80, "saving": 10},
    #     {"offer":"RRRQ", "price": 3*items["R"], "saving": items["Q"]},
    #     {"offer":"UUUU", "price": 3*items["U"], "saving": items["U"]},
    #     {"offer":"VV", "price": 90, "saving": 10},
    #     {"offer":"VVV", "price": 130, "saving": 20},
    # ]


    offers = [
        {"items":"AAA", "price": 130, "saving": 20},
        {"items":"AAAAA", "price": 200, "saving": 50},
        {"items":"EEB", "price": 2*items["E"], "saving": items["B"]},
        ]

    offers_sorted = sorted(offers, key=lambda item: item["saving"], reverse=True)

    for offer in offers:
        for i in offer["items"]:
            count = offer["items"].count(i)
            offer[i] = count

    basket = {}
    for i in skus:
        count = skus.count(i)
        basket[i] = count


    print(offers)
    print(basket)






   

checkout(skus)


