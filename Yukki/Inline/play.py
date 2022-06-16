from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto,Message)

from Yukki import db_mem


def url_markup2(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎵 ᴘʟᴀʏ ᴍᴜsɪᴄ",
                callback_data=f"Yukki {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ᴘʟᴀʏ ᴠɪᴅᴇᴏ  🎥",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],        
        [
            InlineKeyboardButton(
                text=" ᴄʟᴏsᴇ ",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons           
        

def url_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎵 ᴘʟᴀʏ ᴍᴜsɪᴄ",
                callback_data=f"Yukki {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="ᴘʟᴀʏ ᴠɪᴅᴇᴏ 🎥",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=" ᴄʟᴏsᴇ ",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def search_markup(
    ID1,
    ID2,
    ID3,
    ID4,
    ID5,
    duration1,
    duration2,
    duration3,
    duration4,
    duration5,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="1️⃣", callback_data=f"bdrl {ID1}|{duration1}|{user_id}"
            ),
            InlineKeyboardButton(
                text="2️⃣", callback_data=f"bdrl {ID2}|{duration2}|{user_id}"
            ),
            InlineKeyboardButton(
                text="3️⃣", callback_data=f"bdrl {ID3}|{duration3}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="4️⃣", callback_data=f"bdrl {ID4}|{duration4}|{user_id}"
            ),
            InlineKeyboardButton(
                text="5️⃣", callback_data=f"bdrl {ID5}|{duration5}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="➡️", callback_data=f"popat 1|{query}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴄʟᴏsᴇ", callback_data=f"forceclose {query}|{user_id}"
            ),
        ],
    ]
    return buttons


def search_markup2(
    ID6,
    ID7,
    ID8,
    ID9,
    ID10,
    duration6,
    duration7,
    duration8,
    duration9,
    duration10,
    user_id,
    query,
):
    buttons = [
        [
            InlineKeyboardButton(
                text="6️⃣",
                callback_data=f"bdrl {ID6}|{duration6}|{user_id}",
            ),
            InlineKeyboardButton(
                text="7️⃣",
                callback_data=f"bdrl {ID7}|{duration7}|{user_id}",
            ),
            InlineKeyboardButton(
                text="8️⃣",
                callback_data=f"bdrl {ID8}|{duration8}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="9️⃣",
                callback_data=f"bdrl {ID9}|{duration9}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🔟",
                callback_data=f"bdrl {ID10}|{duration10}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️", callback_data=f"popat 2|{query}|{user_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ᴄʟᴏsᴇ", callback_data=f"forceclose {query}|{user_id}"
            ),
        ],
    ]
    return buttons
   

def secondary_markup(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="•ᴍᴇɴᴜ•", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(text="•ᴄʜᴀɴɴᴇʟ•", url=f"https://t.me/RuangTerbukaa"
            ),      
            InlineKeyboardButton(text="•ᴄʟᴏsᴇ•", callback_data=f'close')
            ],
    ]
    return buttons
        


def secondary_markup2(videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="•ᴍᴇɴᴜ•", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(text="•ᴄʜᴀɴɴᴇʟ•", url=f"https://t.me/RuangTerbukaa"   
            ),
        ],
        [
            InlineKeyboardButton(text="•ᴄʟᴏsᴇ•", callback_data=f"close"),
        ],
    ]
    return buttons


def primary_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text="•ᴍᴇɴᴜ•", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(text="•ᴄʜᴀɴɴᴇʟ•", url=f"https://t.me/{SUP_CHANNEL}"
            ),      
            InlineKeyboardButton(text="•ᴄʟᴏsᴇ•", callback_data=f'close')
            ],
    ]
    return buttons


def timer_markup(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text="•ᴍᴇɴᴜ•", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(text="•ᴄʜᴀɴɴᴇʟ•", url=f"https://t.me/RuangTerbukaa"
            ),
            InlineKeyboardButton(text="•ᴄʟᴏsᴇ•", callback_data=f'close')
            ],
    ]
    return buttons


def audio_markup(videoid, user_id, current_time, total_time):
    if videoid not in db_mem:
        db_mem[videoid] = {}
    db_mem[videoid]["check"] = 2
    buttons = [
        [
            InlineKeyboardButton(
                text="•ᴍᴇɴᴜ•", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(text="•ᴄʜᴀɴɴᴇʟ•", url=f"https://t.me/RuangTerbukaa"
            ),
            InlineKeyboardButton(text="•ᴄʟᴏsᴇ•", callback_data=f'close')
            ],
    ]
    return buttons


def audio_timer_markup_start(videoid, user_id, current_time, total_time):
    buttons = [
        [
            InlineKeyboardButton(
                text="•ᴍᴇɴᴜ•", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(text="•ᴄʜᴀɴɴᴇʟ•", url=f"https://t.me/RuangTerbukaa"
            ),
            InlineKeyboardButton(text="•ᴄʟᴏsᴇ•", callback_data=f'close')
            ],
    ]
    return buttons


audio_markup2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="•ᴍᴇɴᴜ•", switch_inline_query_current_chat=""
            ),
            InlineKeyboardButton(text="•ᴄʜᴀɴɴᴇʟ•", url=f"https://t.me/RuangTerbukaa"
            ),
        ],
        [InlineKeyboardButton("•ᴄʟᴏsᴇ•", callback_data="close")],
    ]
)
