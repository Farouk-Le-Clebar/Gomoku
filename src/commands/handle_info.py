import protocol

def handle_info(msg: str) -> None:
    parsed_input = msg.split()
    if len(parsed_input) != 3:
        print("ERROR message - Wrong number of arguments")
        return

    key = parsed_input[1]
    value = parsed_input[2]

    if key not in protocol.settings:
        print("ERROR message - Key is wrong")
        return

    try:
        protocol.settings[key] = int(value)
        return
    except ValueError:
        print("ERROR message - Value is not an integer")
