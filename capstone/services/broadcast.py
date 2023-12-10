from bot_instance import bot
from database.user_db import get_all_drivers_id

async def alert_drivers(booking_id, current_location, destination):
    drivers = get_all_drivers_id()

    for driver_id in drivers:
        try:
            message_text = f"New ride request!\nBooking ID: {booking_id}\nLocation: {current_location}\nDestination: {destination}"
            await bot.send_message(driver_id, message_text)
        except Exception as e:
            print(f"Error sending message to driver {driver_id}: {e}")


async def alert_user(passenger_id, message_text):
    try: 
        await bot.send_message(passenger_id, message_text)
    except Exception as e:
        print(f"Error sending message to user {passenger_id}: {e}")

async def rate_passenger():
    pass

async def rate_driver():
    pass