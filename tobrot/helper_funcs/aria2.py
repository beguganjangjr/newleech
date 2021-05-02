import asyncio
import aria2p
import logging
import os
import re
import requests
from requests import get
from pathlib import Path
from tobrot import ARIA_CONF
LOGGER = logging.getLogger(__name__)

resp = requests.get('https://trackerslist.com/best_aria2.txt')
conf = None
xyza = f"{ARIA_CONF}"


   
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
    #cmd.append(f"--bt-tracker={trackers}")
    if not os.path.exists("apic.conf"):
        with open("apic.conf", "w+", newline="\n", encoding="utf-8") as fole:
            fole.write(xyza)  
            line = open("apic.conf", "r")
            conf_txt = line.read()
            print(conf_txt)
            LOGGER.info(conf_txt)
            cmd.append("--conf-path=apic.conf")
            if "bt-tracker" in conf_txt:
                conf = re.sub("bt-tracker=.*?", "bt-tracker=" + resp.text, conf)
            else:
                conf = conf + "\nbt-tracker=" + resp.text + "\n"
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
