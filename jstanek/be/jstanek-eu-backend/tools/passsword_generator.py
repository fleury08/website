import logging
import string
from dataclasses import dataclass
import random


@dataclass
class PasswordOptions:
    length: int = 16
    lowercase: bool = True
    uppercase: bool = True
    numeric: bool = True
    special: bool = True


def generate_password(psw_opt: PasswordOptions):

    if not psw_opt:
        logging.info("Password options not provided, using default")
        psw_opt = PasswordOptions()

    if psw_opt.length < 1:
        raise ValueError("Invalid password length, must be greater than 0")

    if (
        not psw_opt.lowercase
        and not psw_opt.uppercase
        and not psw_opt.numeric
        and not psw_opt.special
    ):
        raise ValueError("Invalid password options, none selected")

    source_set = ()
    r_pass = ""
    if psw_opt.uppercase:
        source_set += tuple(string.ascii_uppercase)
    if psw_opt.lowercase:
        source_set += tuple(string.ascii_lowercase)
    if psw_opt.numeric:
        source_set += tuple(string.digits)
    if psw_opt.special:
        source_set += tuple(string.punctuation)
    for _ in range(psw_opt.length):
        r_set = random.choice(source_set)
        r_pass += random.choice(r_set)
    return r_pass
