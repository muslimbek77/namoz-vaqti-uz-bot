from aiogram import types
from utils.namoz_vaqti import mintaqalar
from datetime import datetime
from utils.namoz_vaqti import vaqti,oylar
from loader import dp


# Echo bot
@dp.message_handler(text=list(mintaqalar.keys()))
async def bot_echo(message: types.Message):
    month = datetime.now().month
    namoz_vaqti = vaqti(mintaqalar[message.text],month)
    print(namoz_vaqti)
    oy_nomi = oylar[int(namoz_vaqti[0])]
    
    text= f"""Bugun {namoz_vaqti[1]}-{oy_nomi}.\n\n☪️Namoz vaqtlari:\n\nBomdod: {namoz_vaqti[3]}\nQuyosh: {namoz_vaqti[4]}\nPeshin: {namoz_vaqti[5]}\nAsr : 16:57\nShom : {namoz_vaqti[6]}\nXufton : {namoz_vaqti[7]}\n\nManba: islom.uz\n@namoz_uzb_vaqti_bot"""
    
    await message.answer(text=text)
    