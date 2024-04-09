import string
import unittest

from . import passsword_generator


class TestPasswordGenerator(unittest.TestCase):


    def test_lowercase_password(self):
        psw_opt = passsword_generator.PasswordOptions(
            length=10,
            lowercase=True,
            uppercase=False,
            numeric=False,
            special=False,
        )
        psw = passsword_generator.generate_password(psw_opt)
        self.assertEqual(len(psw), 10)
        self.check_for_letter_in_password(psw, string.ascii_lowercase)

    def test_uppercase_password(self):
        psw_opt = passsword_generator.PasswordOptions(
            length=10,
            lowercase=False,
            uppercase=True,
            numeric=False,
            special=False,
        )
        psw = passsword_generator.generate_password(psw_opt)
        self.assertEqual(len(psw), 10)
        self.check_for_letter_in_password(psw, string.ascii_uppercase)

    def test_numeric_password(self):
        psw_opt = passsword_generator.PasswordOptions(
            length=10,
            lowercase=False,
            uppercase=False,
            numeric=True,
            special=False,
        )
        psw = passsword_generator.generate_password(psw_opt)
        self.assertEqual(len(psw), 10)
        self.check_for_letter_in_password(psw, string.digits)

    def test_special_password(self):
        psw_opt = passsword_generator.PasswordOptions(
            length=10,
            lowercase=False,
            uppercase=False,
            numeric=False,
            special=True,
        )
        psw = passsword_generator.generate_password(psw_opt)
        self.assertEqual(len(psw), 10)
        self.check_for_letter_in_password(psw, string.punctuation)

    def check_for_letter_in_password(self, psw, set_of_letters):
        for letter in set_of_letters:
            if letter in psw:
                break
        else:
            self.fail(f"Password does not contain any letters from set ({set_of_letters})")

    def test_generate_password(self):
        psw_opt = passsword_generator.PasswordOptions()
        psw_opt.length = 10
        psw_opt.lowercase = True
        psw_opt.uppercase = True
        psw_opt.numeric = True
        psw_opt.special = True
        psw = passsword_generator.generate_password(psw_opt)
        self.assertEqual(len(psw), 10)
        self.check_for_letter_in_password(psw, string.ascii_lowercase)
        self.check_for_letter_in_password(psw, string.ascii_uppercase)
        self.check_for_letter_in_password(psw, string.digits)
        self.check_for_letter_in_password(psw, string.punctuation)
