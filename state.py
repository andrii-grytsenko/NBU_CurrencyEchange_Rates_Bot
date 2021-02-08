import keyboard as kbd

STATES = {
    "START": {
        "description": "Initial state",
        "keyboard": kbd.kbd_main_screen,
        "message": """
Welcome!

I am ready to inform You about actual currency exchange rates provided by National bank of Ukraine.
Let's start. Choose currency.\n
        """
    },
    "STATE01": {
        "description": "Main menu",
        "keyboard": kbd.kbd_main_screen,
        "message": "Choose currency:"
    },
    "STATE02": {
        "description": "All currencies",
        "keyboard": kbd.kbd_all_currencies,
        "message": "Choose currency:"
    }
}
