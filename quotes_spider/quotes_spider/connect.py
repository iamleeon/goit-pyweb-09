from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read("config.ini")


mongo_user = config.get("DB", "user")
mongo_pass = config.get("DB", "pass")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")


connect(host=f"""mongodb+srv://osandr:*****@scrapped-quotes-and-aut.2khl4.mongodb.net/?retryWrites=true&w=majority&appName=scrapped-quotes-and-authors""", ssl=True)
