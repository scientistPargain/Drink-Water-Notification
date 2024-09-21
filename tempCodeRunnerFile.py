import os
from win10toast_click import ToastNotifier
import webbrowser

def on_notification_click():
    webbrowser.open("https://www.example.com/learn-about-hydration")
    return 0  # Explicitly return an integer value

icon_path = os.path.join(os.curdir, 'icon1.ico')
toaster = ToastNotifier()
toaster.show_toast(
    title="Please Drink Water Now!!",
    msg="The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
    icon_path='icon1.ico',  # Icon path
    duration=10,  # Notification duration in seconds
    threaded=True,  # To allow interaction
    callback_on_click=on_notification_click  # Open URL when clicked
)