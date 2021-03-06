import re
import random

from src.utilities import *
from src import users, channels, debuglog, errlog, plog
from src.functions import get_players, get_all_players
from src.decorators import cmd, event_listener
from src.containers import UserList, UserSet, UserDict, DefaultUserDict
from src.messages import messages
from src.events import Event

from src.roles._mystic_helper import setup_variables

LAST_COUNT = setup_variables("mystic", send_role=True, types=("wolves",))

@event_listener("get_special")
def on_get_special(evt, var):
    # mystics count as special even though they don't have any commands
    evt.data["villagers"].update(get_players(("mystic",)))

# vim: set sw=4 expandtab:
