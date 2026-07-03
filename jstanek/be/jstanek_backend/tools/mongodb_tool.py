from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class MongoDbContainer:
    object_id: str


def mongo_id_parse(mdb_obj: MongoDbContainer) -> datetime:
    if not mdb_obj:
        raise ValueError("Invalid mongo id container, cant parse")

    if not mdb_obj.object_id:
        raise ValueError("Invalid mongo id, cant parse")

    if len(mdb_obj.object_id) == 24:
        timestamp = int(mdb_obj.object_id[:8], 16)
        return datetime.fromtimestamp(timestamp)

    raise ValueError("Invalid mongo id, not 24 characters")
