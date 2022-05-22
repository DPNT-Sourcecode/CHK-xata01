skus = "AAAABBCD"

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price = {"A": 50, "B": 30, "C": 20, "D": 15}
    letters = "ABCD"
    total = 0

    for s in letters:
        count = skus.count(s)
        
        if s == "A":
            offers = count // 3
            total += offers * 130
            non_offers = count % 3
            total += non_offers * price[s]

        elif s == "B":
            offers = count // 2
            total += offers * 45
            non_offers = count % 2
            total += non_offers * price[s]

        else:
            total += count * price[s]

    print(total)


checkout(skus)


