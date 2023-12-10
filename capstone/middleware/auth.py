from aiogram import types
from bot_instance import bot
from aiogram import BaseMiddleware
from database.user_db import get_user_by_id

class AuthMiddleware(BaseMiddleware):
   async def __call__(self, handler, event: types.Message, data: dict):
       user_id = event.from_user.id
       if not await self.is_authenticated(user_id):
           try:
               await bot.send_message(user_id, "You are not authenticated. Please use /start to authenticate.")
               return
           except:
               pass # Ignore Unauthorized exception if the bot is blocked by the user
        #    raise types.MessageSkip()
       return await handler(event, data)

   async def is_authenticated(self, user_id):
       # Replace this with your authentication logic
       user_data = get_user_by_id(user_id)
       return user_data is not None

  
    
def add_middleware(router):
    router.message.middleware(AuthMiddleware())
