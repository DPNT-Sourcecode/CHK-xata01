skus = "AAAABBCD"

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    price = {"A": 50, "B": 30, "C": 20, "D": 15}

    letters = "ABCD"

    for s in letters:
        count = skus.count(s)
        print(count)


checkout(skus)

