def handle_about(msg: str) -> None:
    if len(msg.split()) != 1:
        print("ERROR message - command about just accept 1 argument")
        return

    bot_name = "TTM"
    print(f'name="{bot_name}", version="1.0" author="TTM", country="FR"')
