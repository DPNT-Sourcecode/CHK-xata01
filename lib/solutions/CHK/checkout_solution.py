skus = "AABBBBBAAAB"

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40}
    letters = list(price.keys())

    total = 0

    for s in skus:
        if s not in letters:
            return(-1)

    for s in letters:
        count = skus.count(s)
        
        if s == "A":
            offer1s = count // 5
            total += offer1s * 200
            offer2s = (count % 5) // 3
            total += offer2s * 130
            non_offers = (count % 5) % 3
            total += non_offers * price[s]

            # offers = count // 3
            # total += offers * 130
            # non_offers = count % 3
            # total += non_offers * price[s]

        elif s == "B":
            offers = count // 2
            total += offers * 45
            non_offers = count % 2
            total += non_offers * price[s]

        else:
            total += count * price[s]

    return(total)

checkout(skus)

