from bridge.devices import DeviceBase


class RemoteBase:
    def __init__(self, device: DeviceBase):
        self.device = device

    def turn_on(self):
        self.device.turn_on()

    def turn_off(self):
        self.device.turn_off()

    def set_channel(self, channel):
        self.device.set_channel(channel)
