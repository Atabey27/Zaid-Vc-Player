## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME=BAC98_V4FhQXE-pGQ0EsdLd9yoTciVDvzT-_vXH5dgq3kL16JLhubUKKuLQffu6NClKsj3Z_RPZ6KHE7rk3z9kAd5opYjEMAAeSLf5ynfhpOTq8vNJblHPRgkhgwcj1MmBhHfmbw7fZq5Y066JtKfr6_0FivB-k5o4jBwZRrs7giif0i6DQdgjzbw31SODae4gsYEzGkIVS_nrGCKSQOOxgeEf_Y41j5JnjlIsiJmLi1PrWLf8NRCmYxfUWtxfYZ-drYE8ouf1Sv0om5WLCTpAeoQ5JlCDtm_K4GxxQ_N18rK9afPtLFQVvXKDpe1HctejXa2MUZ9ngOJseslMnXwJrUTKJLtgA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "6374624814:AAEKpIzru9w_ww4Oz5G8fvn7ueA5h1IJWTc")
BOT_NAME = getenv("BOT_NAME", "Müzik botu")

API_ID = int(getenv("API_ID", "1148427"))
API_HASH = getenv("API_HASH", "362406c73185652edcf9942fde49719c")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Atabey27:Harun.27@cluster0.fmkdwd4.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Atabey")
OWNER_USERNAME = getenv("OWNER_USERNAME", "GokyuZu")
ALIVE_NAME = getenv("ALIVE_NAME", "Atabey")
BOT_USERNAME = getenv("BOT_USERNAME", "Muzikcalarxbot")
OWNER_ID = getenv("OWNER_ID", "1285704630")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Atabey_Asistan")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "1969816894")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "1969816894")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1285704630").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
