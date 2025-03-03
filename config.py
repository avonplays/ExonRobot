from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", "26603995"))
    API_HASH = getenv("API_HASH", "970f6f249c22ea4710927f3485f149f8")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "7667702659:AAHPIU2yQEMrbOu696qO93VaKcg92h6j5DM")
    OWNER_ID = int(getenv("OWNER_ID", "6289029511"))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Yash_747")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "AbishnoiMF")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002288846111"))
    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://Avon:Avon@avon.fstai.mongodb.net/?retryWrites=true&w=majority",
    )
    DB_NAME = getenv("DB_NAME", "Avon")
    REDIS_URL = "redis://default:3cmDFTT9nIbpV2Of5iH9RolC4AcDD3JR@redis-15566.crce182.ap-south-1-1.ec2.redns.redis-cloud.com:15566"
    DATABASE_URL = getenv("DATABASE_URL", "postgres://qszfsijv:y6sYqkEb8Z9lFGBmriG7AYjbSbgAJBVk@peanut.db.elephantsql.com/qszfsijv")

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
