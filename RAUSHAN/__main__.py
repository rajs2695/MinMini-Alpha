import asyncio
import importlib

from heartbeat import heartbeat
from pyrogram import Client, idle
from RAUSHAN.helper import join
from RAUSHAN.modules import ALL_MODULES
from RAUSHAN import clients, app, ids

async def start_bot():
    await app.start()
    print("LOG: Founded Bot token Booting Zeus.")
    for all_module in ALL_MODULES:
        importlib.import_module("RAUSHAN.modules" + all_module)
        print(f"Successfully Imported {all_module} 💥")
    for cli in clients:
        try:
            await cli.start()
            ex = await cli.get_me()
            await join(cli)
            print(f"Started {ex.first_name} 🔥")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()

loop = asyncio.get_event_loop()
heartbeat()
loop.run_until_complete(start_bot())
