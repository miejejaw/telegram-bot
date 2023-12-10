from database.booking_db import insert_booking, update_driver_col, delete_booking, get_booking, get_booking_by_passenger_id
from services.broadcast import alert_drivers, alert_user, rate_driver, rate_passenger
from database.history_db import insert_to_history, get_history_by_passenger_id


async def booking_ride(user_id, current, destination):
    booking_id = insert_booking(user_id, current, destination)
    await alert_drivers(booking_id, current, destination)
    return booking_id
    
async def accept_ride(booking_id, driver_id):
    res = get_booking(int(booking_id))
    if res[2] == "none":
        update_driver_col(booking_id, f"{driver_id} is coming for you!")
        await alert_user(res[1], driver_id)
        return "well done! go for your client"
    
    return "The book already taken, sorry!"

async def finish_ride(passenger_id):
    res = get_booking_by_passenger_id(passenger_id)
    if not res: 
        return "you didn't book a ride!"
    insert_to_history(res)
    await rate_passenger(res[1], res[2])
    return "Thanks for using our platform!"

async def cancel_ride(passenger_id):
    res = get_booking_by_passenger_id(passenger_id)
    if not res: 
        return "you didn't book a ride!"
    
    delete_booking(int(res[0]))
    if res[2] != "none":
        await alert_user(res[2], f"The passenger canceled {res[0]} booking")
    
    return "successfully booking canceled!"


async def rate_user(passenger_id, driver_id):
    await alert_user(passenger_id, f"How were your driver, rate {driver_id}")
    await alert_user(driver_id, f"How were your passenger, rate {passenger_id}")
    
def get_user_history(user_id):
    res = get_history_by_passenger_id(user_id)
    return res