import asyncio
import aria2p
import logging
import os
import re
from requests import get
from pathlib import Path
from tobrot import ARIA_CONF
LOGGER = logging.getLogger(__name__)

trackers_list = get(
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt"
).text.replace("\n\n", ",")
trackers = f"[{trackers_list}]"


async def aria_start():
    cmd = [
        "aria2c",
        "--enable-rpc=true"
        ]
    cmd.append("--daemon=true")
    cmd.append("--follow-torrent=mem")
    cmd.append("--max-connection-per-server=10")
    cmd.append("--rpc-listen-all=false")
    cmd.append("--rpc-listen-port=6800")
    cmd.append("--seed-time=0")
    cmd.append(f"--bt-tracker={trackers}")
    if not os.path.exists("apic.conf"):
        with open("apic.conf", "w+", newline="\n") as fole:
            fole.write(f"{ARIA_CONF}")            
            line = fole.read()
            print(line)
            LOGGER.info(line)
            #cmd.append("--conf-path=/app/apic.conf")
#            print(important)
            
    LOGGER.info(cmd)
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    LOGGER.info(stderr or stdout)
    aria2 = aria2p.API(
        aria2p.Client(
            host="http://localhost",
            port=6800
        )
    )
    return aria2
