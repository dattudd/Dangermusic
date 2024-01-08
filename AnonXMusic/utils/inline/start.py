from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["𝐆𝐫𝐨𝐮𝐩"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["𝐎𝐰𝐧𝐞𝐫"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["𝐆𝐫𝐨𝐮𝐩"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["𝐔𝐩𝐝𝐚𝐭𝐞𝐬📢"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_7"], url=config.UPSTREAM_REPO),
        ],
    ]
    return buttons
