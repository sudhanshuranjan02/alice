import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 26166806
API_HASH = "910ec76cc936a4835d894349318f2af4"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8013132141:AAF0emnwEdwSdkiPv6AhYStYHnaqDybjCpg"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://sudhanshuranjan664:@khushi74@cluster0.8wuwyj4.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002782996944

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 8128691649

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/+sQUkp886Dt41MmE9"
SUPPORT_GROUP = "https://t.me/+sQUkp886Dt41MmE9"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQGPRhYAaSd89ggM-1g4C-HSyr_pckO-FChMslMo2wKVMHPX58OBq8PMD6mU3o7jwhjOObzsZmzQ999XbIzEwDx3F9n5cvFR9wxlbgBGdL41yc7ZfAbttQuWvWXNQgBijZIRpsJJM1iC6QDBHdEBxvvXfRmJdVUgGnfYhnyiMGM_2Tl0-Xug5BxDPhaPfWLLbGJCe2q8CK3tf_qukO9ojkcUk1ICBLiz4v7at0dDJux3_IL9-UH2NSK6LBdWrcOK69m4V55X0LFYTIWAVs52B7LtkD9kDeVIbHmxzMwCWfE0x-RYBFdLAg7O7sA-65xLzAPOI964WNBZkpO-0i6CeDP3BbyXiAAAAAHdnrFtAQ"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"

PING_IMG_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"
STATS_IMG_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"
STREAM_IMG_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/d9c630a0992561bee5889-5c2b76374d253d3b8d.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
