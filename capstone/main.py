import asyncio
from aiogram import Dispatcher
from bot_instance import bot
from middleware.auth import add_middleware
from handlers.signup_handler import register_router
from handlers.user_handler import user_router
from handlers.booking_handler import booking_router
from handlers.accept_ride import accept_router
from handlers.cancel_ride import cancel_router
from handlers.rate_driver_handler import rate_driver_router
from handlers.rate_passenger_handler import rate_passenger_router
from handlers.finish_ride_handler import finish_ride_router
from handlers.view_user_history_hadler import view_user_history_router
# from handlers.login_handler import auth_router


def register_routers(dp: Dispatcher) -> None:
    # add router to middleware
    add_middleware(user_router)
    add_middleware(booking_router)
    add_middleware(accept_router)
    add_middleware(cancel_router)
    add_middleware(rate_passenger_router)
    add_middleware(rate_driver_router)
    add_middleware(finish_ride_router)
    add_middleware(view_user_history_router)
    
    # register routers
    dp.include_router(register_router)
    dp.include_router(user_router)
    dp.include_router(booking_router)
    dp.include_router(accept_router)
    dp.include_router(cancel_router)
    dp.include_router(rate_passenger_router)
    dp.include_router(rate_driver_router)
    dp.include_router(finish_ride_router)
    dp.include_router(view_user_history_router)
    

async def main() -> None:
    dp = Dispatcher()
    register_routers(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())