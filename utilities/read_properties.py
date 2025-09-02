import configparser

config = configparser.ConfigParser()
config.read("./configurations/config.ini")


class ReadConfig:

    @staticmethod
    def get_admin_page_url():
        url = config.get("admin login info", "admin_page_url")
        return url

    @staticmethod
    def get_username():
        username = config.get("admin login info", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("admin login info", "password")
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get("admin login info", "invalid_username")
        return invalid_username

    @staticmethod
    def get_valid_firstname():
        firstname = config.get("place order", "firstname")
        return firstname

    @staticmethod
    def get_valid_lastname():
        lastname = config.get("place order", "lastname")
        return lastname

    @staticmethod
    def get_postalcode():
        postalcode = config.get("place order", "postalcode")
        return postalcode
