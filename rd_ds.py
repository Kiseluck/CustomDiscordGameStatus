from pypresence import Presence
from time import time

RPC = Presence("ключ")
btns = [
    {
        "label": "Discord",
        "url": "https://discord.gg/Qnkrx4K2Mm"
    },
    {
        "label": "Сайт",
        "url": "https://shop.riven-dell.ru"
    }
]



RPC.connect()
while True:
    RPC.update(state="Вк: vk.com/riven_dell", details="Лучший сервер Minecraft", start=time(), buttons=btns, large_image="1", large_text="mc.riven-dell.ru")
