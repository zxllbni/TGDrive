from dotenv import load_dotenv
import os

# Load environment variables from the .env file, if present
load_dotenv()

# Telegram API credentials obtained from https://my.telegram.org/auth
API_ID = int(os.getenv("API_ID","22419004"))  # Your Telegram API ID
API_HASH = os.getenv("API_HASH","34982b52c4a83c2af3ce8f4fe12fe4e1")  # Your Telegram API Hash

# List of Telegram bot tokens used for file upload/download operations
BOT_TOKENS = os.getenv("BOT_TOKENS", "7373559684:AAHm9PoxfB7IJolFUZCwCLM-kJD3rd59GqM").strip(", ").split(",")
BOT_TOKENS = [token.strip() for token in BOT_TOKENS if token.strip() != ""]

# List of Premium Telegram Account Pyrogram String Sessions used for file upload/download operations
STRING_SESSIONS = os.getenv("STRING_SESSIONS", "BQFWFjwAdgqS_wMzC0FjA0WtIhcnDcNDlDB4OdrNrFOYmmTURa9e9rggMX2Y-tCOcVfqgZ8kVvTPCdA-9iY6Yt3C1nGFb9Ax-jS8vIYwPqkhNN00ON_ttC2ZEiLc4Yi3aMddiHFixXeJZzNYRn4SZ8qn9s5yQfDskx3g9G9qPK7WeSDWOB0yv2k8R1ySIsgWT3U852MIFygWnOUMT7O9QUR3-cG6CrIyFSiGqCOBJEuz8brepYCEYaNf37k3nGkuXuPhNl4b1ESU-_duMir2QOhFBV5IU9TKUrAIFhR-io5oLkLQbCC3cdKAHosvQ5A14XxAeJgeD36qYlmasWHwt6ybR5UEzQAAAAGR2xqSAA").strip(", ").split(",")
STRING_SESSIONS = [
    session.strip() for session in STRING_SESSIONS if session.strip() != ""
]

# Chat ID of the Telegram storage channel where files will be stored
STORAGE_CHANNEL = int(os.getenv("STORAGE_CHANNEL","-1002235500749"))  # Your storage channel's chat ID

# Message ID of a file in the storage channel used for storing database backups
DATABASE_BACKUP_MSG_ID = int(
    os.getenv("DATABASE_BACKUP_MSG_ID")
)  # Message ID for database backup

# Password used to access the website's admin panel
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "noob")  # Default to "admin" if not set

# Determine the maximum file size (in bytes) allowed for uploading to Telegram
# 1.98 GB if no premium sessions are provided, otherwise 3.98 GB
if len(STRING_SESSIONS) == 0:
    MAX_FILE_SIZE = 1.98 * 1024 * 1024 * 1024  # 2 GB in bytes
else:
    MAX_FILE_SIZE = 3.98 * 1024 * 1024 * 1024  # 4 GB in bytes

# Database backup interval in seconds. Backups will be sent to the storage channel at this interval
DATABASE_BACKUP_TIME = int(
    os.getenv("DATABASE_BACKUP_TIME", 60)
)  # Default to 60 seconds

# Time delay in seconds before retrying after a Telegram API floodwait error
SLEEP_THRESHOLD = int(os.getenv("SLEEP_THRESHOLD", 60))  # Default to 60 seconds

# Choose whether to use .session files for session persistence or in-memory sessions
# Set to False to use in-memory sessions instead of .session files
USE_SESSION_FILE = bool(
    os.getenv("USE_SESSION_FILE", True)
)  # Default to True (use .session files)


# Domain to auto-ping and keep the website active
WEBSITE_DOMAIN = os.getenv("WEBSITE_DOMAIN", None)
