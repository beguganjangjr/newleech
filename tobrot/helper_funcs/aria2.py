import asyncio
import aria2p
import logging

LOGGER = logging.getLogger(__name__)
__config = {
    "dir" : "downloads",
    "daemon" : "true",
    "max-connection-per-server" : "16",
    "max-overall-upload-limit" : "1K",
    "max-concurrent-downloads" : "3",
    "bt-max-peers" : "0",
    "rpc-listen-all" : "false",
    "rpc-listen-port": "6800",
    "seed-ratio" : "0",
    "seed-time" : "0.01"
}


async def aria_start():
    cmd = ["aria2c",
          "--enable-rpc"]
    cmd.append(f"--{__config}")
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
