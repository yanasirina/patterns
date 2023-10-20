import devices
import remotes

"""
Создадим устройства и попробуем управлять ими разными средствами. 
Например, включить устройство используя пульт, а выключить, используя мобильное приложение.
"""

radio = devices.Radio()
remote_control_for_radio = remotes.RemoteControl(device=radio)
mobile_app_for_radio = remotes.MobileApp(device=radio)
remote_control_for_radio.turn_on()
mobile_app_for_radio.turn_off()

tv = devices.TV()
remote_control_for_tv = remotes.RemoteControl(device=tv)
mobile_app_for_tv = remotes.MobileApp(device=tv)
mobile_app_for_tv.turn_on()
remote_control_for_tv.turn_off()
