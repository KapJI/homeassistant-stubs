class USBDevice:
    device: str
    vid: str
    pid: str
    serial_number: Union[str, None]
    manufacturer: Union[str, None]
    description: Union[str, None]
    def __init__(self, device, vid, pid, serial_number, manufacturer, description) -> None: ...
