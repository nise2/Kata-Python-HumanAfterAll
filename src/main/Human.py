from enums.Sex import Sex

class Human:
    def __init__(self, social_security_number):
        self.social_security_number = social_security_number
        self.sex = Sex.MALE if self.social_security_number.replace(" ", "")[0] == "1" else Sex.FEMALE
        self.year_of_birth = self.get_year_of_birth()
        self.month_of_birth = self.social_security_number.replace(" ", "")[3:5]
        self.place_of_birth = self.social_security_number.replace(" ", "")[-2:]

    def get_year_of_birth(self):
        year = self.social_security_number.replace(" ", "")[1:3]
        return f"20{year}" if int(year) <= 15 else f"19{year}"

