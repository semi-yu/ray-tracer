import os

from dotenv import load_dotenv


load_dotenv("./config.env")

class Config:
    HEIGHT = int(os.getenv("HEIGHT"))
    WIDTH = int(os.getenv("WIDTH"))
