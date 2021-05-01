import asyncio
import aria2p
import logging
import os
from pathlib import Path
from tobrot import ARIA_CONF
LOGGER = logging.getLogger(__name__)



async def aria_start():
    cmd = ["aria2c",
          "--enable-rpc"]
    if not os.path.exists("apic.conf"):
        with open("apic.conf", "w+", newline="\n", encoding="utf-8") as fole:
            fole.write(f"{ARIA_CONF}")
    if os.path.exists("apic.conf"):
         with open("apic.conf", "r+") as file:
                con = file.read()
                gUP = re.findall("\[(.*)\]", con)[0]
                LOGGER.info(gUP)
    cmd.append("--conf-path=/app/apic.conf")
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
