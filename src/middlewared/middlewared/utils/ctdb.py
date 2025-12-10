import os
from json import dumps
from typing import TypedDict

# CTDB state directory should be a on per-node persistent filesystem
# This is placed on a filesystem that doesn't persist across upgrades
CTDB_DATA_DIR = '/var/lib/ctdb'
CTDB_RUN_DIR = '/var/run/ctdb'

VOLATILE_DB = os.path.join(CTDB_RUN_DIR, 'volatile')
PERSISITENT_DB = os.path.join(CTDB_DATA_DIR, 'persistent')
STATE_DB = os.path.join(CTDB_DATA_DIR, 'state')
RECLOCK_FILE_PATH = os.path.join(CTDB_RUN_DIR, 'reclock.config.json')
RECLOCK_HELPER_SCRIPT = '/usr/bin/ctdb_ha_reclock.py'


class TruenasHaReclockConfig(TypedDict):
    pool: str


def write_reclock_file(config: TrueNASHaReclockConfig) -> None:
    os.makedirs(CTDB_RUN_DIR, mode=0o700, exist_ok=True)

    with open(RECLOCK_FILE_PATH, 'w') as f:
        f.write(dumps(config))
        f.flush()
        os.fsync(f.fileno())
