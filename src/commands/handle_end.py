import protocol

def handle_end(msg: str) -> None:
    protocol.should_stop = True