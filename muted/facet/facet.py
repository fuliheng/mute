
from __future__ import annotations

import json

from pathlib import Path
from typing import Type

from logcat.logcat import LogCat

class Facet:
    @classmethod
    def instance(cls, entity: str, **kwargs) -> Type[Facet]:
        if not entity in cls._cache:
            path = Path(f'{cls.DATA_PATH}/{entity}.json')

            if path.is_file():
                with path.open(encoding='utf-8') as fin:
                    for key, value in json.load(fin).items():
                        cls._cache[key] = cls(value)

                entity = ""
            else:
                cls._cache[entity] = cls(**kwargs)

        return cls._cache[entity]

# facet.py
