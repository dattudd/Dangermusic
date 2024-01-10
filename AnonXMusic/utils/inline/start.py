from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝖠𝖽𝖽 𝖬𝖾 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝖠𝖽𝖽 𝖬𝖾 𝖨𝗇 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["𝖧𝖾𝗅𝗉 𝖠𝗇𝖽 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋"], url=f"https://t.me/mental_pillodu",),
            InlineKeyboardButton(text=_["𝖴𝗉𝖽𝖺𝗍𝖾𝗌 📢"], url=config.SUPPORT_CHAT),
        ],
        [
            
            InlineKeyboardButton(text=_["S_B_7"], url=f"https://telegra.ph/file/1aac4564298f148beca03.jpg"),
        ],
    ]
    return buttons
