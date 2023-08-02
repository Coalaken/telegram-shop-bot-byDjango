from aiogram import Dispatcher


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = ()
    
    for handler in handlers:
        handler(dp)