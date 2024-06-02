import os

API_ID = API_ID = 22223501

API_HASH = os.environ.get("API_HASH", "e78c151d670ab33c5f7f731027c5ab26")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7329591675:AAGaT6f8u-NcGNL4ytq0XTFNkYZL_SS8bd8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6235754855))

LOG = -1002183078146,

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6235754855").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


