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
from functools import partial

loop = asyncio.get_event_loop()


   
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
    cmd.append("--seed-time=0.01")
    #cmd.append(f"--bt-tracker={trackers}")
    #conf = None
    if not os.path.exists("apic.conf"):
        with open("apic.conf", "w+", newline="\n", encoding="utf-8") as fole:
            resp = requests.get('https://trackerslist.com/best_aria2.txt')
            fole.write(f"{ARIA_CONF}")  
            line = open("apic.conf", "r", encoding="utf-8")
            conf = line.read()
            print(conf)
            LOGGER.info(conf)
            
            if "bt-tracker" in conf_txt:
                conf = re.sub("bt-tracker=.*?", "bt-tracker=" + resp.text, conf)
            else:
                conf = conf + "\nbt-tracker=" + resp.text + "\n"
#            print(important)
            cmd.append("--conf-path=apic.conf")
            
    LOGGER.info(cmd)
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    LOGGER.info(stderr or stdout)
    #aria2 = aria2p.API(
     #   aria2p.Client(host="http://localhost", port=ARIA_TWO_STARTED_PORT, secret="")   
    #arcli = await loop.create_task(loop.run_in_executor(None, partial(aria2p.Client, host="http://localhost", port=6800, secret="")))
    #aria2 = await loop.create_task(loop.run_in_executor(None, aria2p.API, arcli)  
    arcli = await loop.run_in_executor(None, partial(aria2p.Client, host="http://localhost", port=6800, secret=""))
    aria2 = await loop.run_in_executor(None, aria2p.API, arcli)  
   
   
    return aria2
