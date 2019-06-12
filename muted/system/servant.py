
from __future__ import annotations

from event.event import Event
from event.handler import Handler
from message.message import Message

from system.channel import Channel
from system.cmd_echo import CmdEcho
from system.cmd_look import CmdLook
from system.cmd_say import CmdSay
from system.sign_in import SignIn
from system.cmd_time import CmdTime
from system.cmd_logout import CmdLogout
from logcat.logcat import LogCat

class Servant(Handler):
    _instance: Servant = None

    @LogCat.log_func
    def __init__(self):
        super().__init__()

        self.on(Message.TEXT, self._on_text)

    @classmethod
    def instance(cls) -> Servant:
        if not cls._instance:
            cls._instance = Servant()

            CmdEcho(cls._instance)
            CmdLook(cls._instance)
            CmdSay(cls._instance)
            CmdTime(cls._instance)
            CmdLogout(cls._instance)
            SignIn(cls._instance)

        return cls._instance

    @LogCat.log_func
    def _on_text(self, e: Event, entity: str, who: str, text: str) -> None:
        words = text.split()

        if len(words):
            Event.trigger(
                Event(words[0], self, entity=entity, args=words[1:])
            )
        else:
            text = f'你要作什麼？'
            Channel.toRole(entity, Message.TEXT, text)

    @LogCat.log_func
    def _on_any(self, e: Event, entity: str, **kwargs) -> None:
        text = f'你要作什麼？'

        Channel.toRole(entity, Message.TEXT, text)

# servant.py
