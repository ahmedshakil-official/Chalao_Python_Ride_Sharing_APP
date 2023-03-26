import random


class BRTA:

    def __init__(self):
        self.__license = {}

    def driving_test(self, email):
        score = random.randint(0, 100)

        if score >= 50:
            print("Congratulations Driver!")
            license_no = random.randint(5000, 9999)
            self.__license[email] = license_no
            return license_no
        else:
            print("Test again!")
            return False

    def validate_license(self, email, license):
        for key, value in self.__license.items():
            if key == email:
                return True
        return False
