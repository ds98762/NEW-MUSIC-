# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯ ᴄʟᴏsᴇ ✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="ʜᴇʟᴩ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="Gʀᴏᴜᴘ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="Aʙᴏᴜᴛ Vɪsʜᴜ", url="https://t.me/abt_mei"
        ),
        InlineKeyboardButton(text="Vɪsʜᴜ", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="Cʜᴀɴɴᴇʟ", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="Gʀᴏᴜᴘ", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="Aʙᴏᴜᴛ Vɪsʜᴜ", url="https://t.me/abt_mei"
        ),
        InlineKeyboardButton(text="Vɪsʜᴜ", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="Eᴠᴇʀʏᴏɴᴇ",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="Sᴜᴅᴏ", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="Oᴡɴᴇʀ", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="Bᴀᴄᴋ", callback_data="fallen_home"),
        InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="Sᴜᴘᴘᴏʀᴛ 🦋", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="Bᴀᴄᴋ", callback_data="fallen_help"),
        InlineKeyboardButton(text="Cʟᴏsᴇ", callback_data="close"),
    ],
]
