skus = "EEBAAAAAAAAA"

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    # item = list(price.keys())
    item = "AEBCD"

    total = 0

    free_Bs = 0

    for s in skus:
        if s not in item:
            return(-1)

    for s in item:
        count = skus.count(s)
        
        if s == "A":
            offer1s = count // 5
            total += offer1s * 200
            offer2s = (count % 5) // 3
            total += offer2s * 130
            non_offers = (count % 5) % 3
            total += non_offers * price[s]
            print(total)

            # offers = count // 3
            # total += offers * 130
            # non_offers = count % 3
            # total += non_offers * price[s]

        elif s == "E":
            free_Bs = count // 2
            print(free_Bs)

        elif s == "B":
            new_count = count - free_Bs
            offers = new_count // 2
            total += offers * 45
            non_offers = new_count % 2
            total += non_offers * price[s]
            print(total)

            # offers = (count // 2) - free_Bs
            # total += offers * 45
            # non_offers = count % 2
            # total += non_offers * price[s]

        else:
            total += count * price[s]
            print(total)

    print(total)

checkout(skus)





