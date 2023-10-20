class DeviceBase:
    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError

    def set_channel(self, channel: int):
        raise NotImplementedError

    def restart(self):
        raise NotImplementedError
