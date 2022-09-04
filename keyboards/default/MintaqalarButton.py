from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.namoz_vaqti import mintaqalar

mintaqa_btn = ReplyKeyboardMarkup(row_width=2)

for i in list(mintaqalar.keys()):
    mintaqa_btn.insert(KeyboardButton(text=i))

