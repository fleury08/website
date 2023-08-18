def generate_password(
    uppercase: bool, lowercase: bool, numbers: bool, symbols: bool, length: int
):
    import string
    import random

    source_set = ()
    r_pass = ""
    if uppercase:
        source_set += tuple(string.ascii_uppercase)
    if lowercase:
        source_set += tuple(string.ascii_lowercase)
    if numbers:
        source_set += tuple(string.digits)
    if symbols:
        source_set += tuple(string.punctuation)
    for s in range(length):
        r_set = random.choice(source_set)
        r_pass += random.choice(r_set)
    return r_pass
