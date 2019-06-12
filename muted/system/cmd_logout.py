
from __future__ import annotations

from typing import Type

from component.name import Name
from component.role import Role
from component.room import Room

from event.event import Event
from message.message import Message
from system.channel import Channel

from logcat.logcat import LogCat
import socket

class CmdLogout:
    @LogCat.log_func
    def __init__(self, servant: Type[Handler]):
        servant.on(Event.CMD_LOGOUT, self._on_cmd_logout)


    @LogCat.log_func
    def _on_cmd_logout(
        self, e: Event, entity: str = '', args: List[str] = []

    ) -> None:

        if not args:
            socket.disconnect()

        else:
            text = f'目前不支援參數請勿輸入任何數值'

            role = Role.instance(entity)
            Channel.toRole(entity, Message.TEXT, text)


# cmd_say.py
