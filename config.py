# config.py

class Config:
    SECRET_KEY = 'ksxr hltz slcv hnsq'  # Change this to a strong key
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'saimani.dodla@gmail.com'
    MAIL_PASSWORD = 'Swapna@14'  # Use an App Password, NOT your actual password
    MAIL_DEFAULT_SENDER = 'saimani.dodla@gmail.com'

# Use this in your Flask app
app_config = Config()

