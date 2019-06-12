
from __future__ import annotations

from typing import List
from typing import Type

from component.name import Name
from component.role import Role

from event.event import Event
from message.message import Message
from system.channel import Channel

from logcat.logcat import LogCat
import time
class CmdTime:
    @LogCat.log_func
    def __init__(self, servant: Type[Handler]):
        servant.on(Event.CMD_TIME, self._on_cmd_time)


    @LogCat.log_func
    def _on_cmd_time(
        self, e: Event, entity: str = '', args: List[str] = []

    ) -> None:
        localtime = time.asctime( time.localtime(time.time()) )
        if not args:
            text = f'現在時間為{" ".join(localtime)}'

            role = Role.instance(entity)
            Channel.toRoom(role.room, Message.TEXT, text)

        else:
            text = f'目前不支援參數請勿輸入任何數值'

            role = Role.instance(entity)
            Channel.toRole(entity, Message.TEXT, text)


# cmd_say.py
