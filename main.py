from helpers.kanye import Kanye
from helpers.config import Auth

Kanye().run(
    token=Auth.token,
    reconnect=True,
)
