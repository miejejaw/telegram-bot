from bot_instance import bot
from database.rate_db import insert_rating, update_rating, get_rating

async def rate(user_id, rate_value):
    res = get_rating(user_id)
    if not res:
        insert_rating(user_id, rate_value)
    else:
        rate = (rate_value+int(res[2]))/2
        update_rating(user_id, str(rate))
    
