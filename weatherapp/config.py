import dataclasses as dc
import os
from dotenv import load_dotenv


@dc.dataclass
class Config:
    token: str


def load_from_env() -> Config:
    load_dotenv()
    return Config(token=os.getenv("WEATHER_TOKEN"))
