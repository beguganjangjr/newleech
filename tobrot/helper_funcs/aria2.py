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
resp = requests.get('https://trackerslist.com/best_aria2.txt')

   
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
      
    if os.path.exists("aria2c.conf"):
      with open("aria2c.conf", "r") as f:
         conf = f.read()        
      if "bt-tracker" in conf:
         conf = re.sub("bt-tracker=.*?", "bt-tracker=" + resp.text, conf)
      else:
         conf = conf + "\nbt-tracker=" + resp.text + "\n"
      #print(conf)
      with open("aria2c.conf", "w+") as f:
         f.write(conf)
         cmd.append("--conf-path=aria2c.conf")         
    elif not os.path.exists("aria2c.conf"):
        with open("aria2c.conf", "w+", newline="\n", encoding="utf-8") as f:
            f.write(f"{ARIA_CONF}")  
            cmd.append("--conf-path=aria2c.conf")
            

         

    else:
      cmd.append(f"--bt-tracker={resp.text}")

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
