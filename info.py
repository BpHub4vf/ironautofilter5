import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '24736263'))
API_HASH = environ.get('API_HASH', '4d53732917b73a6bb89c3b2f2f7b0902')
BOT_TOKEN = environ.get('BOT_TOKEN', "6156393446:AAEj4SJHEkOMs_jGG4FrYIoSO7cVkheuU74")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', 'True'))
PORT = environ.get("PORT", "8080")
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")

PICS = (environ.get('PICS', 'https://telegra.ph/file/9354a124921994bf84d86.jpg https://telegra.ph/file/8233d87aedf440497a428.jpg https://telegra.ph/file/b4ba8852086d311226e1d.jpg https://telegra.ph/file/55c8dbfa80cf494a2af50.jpg https://telegra.ph/file/a5ecb192e1a0cae82412a.jpg https://telegra.ph/file/e3c85682af8c575a78b5d.jpg https://telegra.ph/file/0355bd3a158f22171f2d5.jpg https://telegra.ph/file/b64a61bbe2245c5ca6141.jpg https://telegra.ph/file/c545eaea593e14d256b25.jpg https://telegra.ph/file/a883451badabf41bb5fe8.jpg https://telegra.ph/file/4e2f727e0055e47c19b9e.jpg https://telegra.ph/file/52fbb1e7864a571e7fa23.jpg https://telegra.ph/file/4147c2a1086e6041c31cb.jpg https://telegra.ph/file/72f563d7c4bedf1b2221c.jpg https://telegra.ph/file/a235ea8103a073c3879cf.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/46443096bc6895c74a716.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/b60d2facc538ad82ad22d.jpg")
NEWGRP = environ.get("NEWGRP", "https://telegra.ph/file/705593c3ae56831c8e565.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5257925921 1228255863').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001895151847').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5257925921 1228255863').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('-1001685314725')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
FILDLT_CNL = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('FILDLT_CNL', '0').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://imab7016:katari007@cluster0.zusimxs.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'TELEGRAM_FILE')

# Channel Button Links
GRP_LNK = environ.get('GRP_LNK', '')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/HUB4VF')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
MSG_ALRT = environ.get('MSG_ALRT', 'Share and Support Us')

# Custom Chats
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001649555430'))
FILE_CHANNEL = int(environ.get('FILE_CHANNEL', '-1001895151847'))
FILE_CHANNEL_LINK = environ.get('FILE_CHANNEL_LINK', 'https://t.me/+kJBKQHHb7dk4ZjM9')

# Log Channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001862601820'))
RQST_LOG_CHANNEL = int(environ.get('RQST_LOG_CHANNEL', '-1001862601820'))

# Bot Options
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "⚡<b>File Provided By @HUB4VF</b>⚡\n\n🎦 <b>File Name: </b> ➥  <i>{file_caption}</i>\n⚙️ <b>Size: </b><i>{file_size}</i>\n\n                ❤️<b>WE LOVE YOU</b>❤️\n🔥  ↭ <b>Join Now @HUB4VF</b> ↭  🔥")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Your Query: {query}</b> \n‌‌‌‌IMDb Data by @HUB4VF \n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10 \n\n♥️ we are nothing without you ♥️ \n\n💛 Please Share Us 💛\n\n⚠️Click on the button 👇 below to get your query privately")
CYNITE_IMDB_TEMPLATE = environ.get("KD_IMDB_TEMPLATE", "<b><b>🏷 Tɪᴛʟᴇ</b> : <a href={url}>{title}</a>\n\n🌟 Rᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10\n💀 Rᴇʟᴇᴀsᴇ :  <b>{release_date}</b> <b>{countries}</b>\n\n🎭 Gᴇɴʀᴇs : <b>{genres}</b></b>\n\n<b>📖 Sᴛᴏʀʏ Lɪɴᴇ :</b> <code>{plot}</code>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001768336853')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

# Auto Delete , Filter & Auto Filter
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
MAUTO_DELETE = is_enabled((environ.get('MAUTO_DELETE', "True")), True)

# Delete Time
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
SPL_DELETE_TIME = int(environ.get('SPL_DELETE_TIME', 15))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
