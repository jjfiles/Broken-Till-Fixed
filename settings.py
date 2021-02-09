from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv("SECRET")
LOCAL = os.getenv("LOCAL")