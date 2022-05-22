skus = "EEEBBAAAAAAAAA"

skus = "EEBAAAEEBA"

skus = "EEEEBBAAA"

# skus = "FFFFFF"

# skus = "AAAEEB"

skus = "AAA"

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
        {"name":"AAA", "price": 130, "saving": 20},
        {"name":"AAAAA", "price": 200, "saving": 50},
        {"name":"EEB", "price": 2*items["E"], "saving": items["B"]},
        ]

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

    # print(offers_sorted)
    print(basket)
    total = 0
    offers_used = 0
    offers_used_repeat = -1

    while counter > 0:

        for offer in offers_sorted:
            keys=(list(offer["items"].keys()))
            check = 0

            temp_basket = basket
            leave_loop = False
            remaining_items = 0

            for key in keys:
                try:
                    if temp_basket[key] >= offer["items"][key]:
                        temp_basket[key] = temp_basket[key] - offer["items"][key]
                        check += 1

                    if check == len(keys):
                        total += offer["price"]
                        offers_used += 1
                        leave_loop = True

                except:
                    pass

            if leave_loop == True:
                continue

            if offers_used_repeat == offers_used:
                for key, value in basket.items():
                    total += items[key] * value
                    print('+')
                counter = 0
                print('0')
                print(counter)
                # return

            offers_used_repeat = offers_used


        basket = temp_basket

        # counter = sum(basket.values())

        # if counter 

        # for item in basket:
        #     print(item)


        # print(basket)
        # print(counter)
        # print(total)

        # return
    print(basket)
    print(total)
            
            









   

checkout(skus)



