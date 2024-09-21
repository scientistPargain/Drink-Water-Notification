
import time
import webbrowser 
from plyer import notification 
import os
print(os.curdir)
os.chdir(r'C:\Users\deepa\Desktop\Projects\Python\DesktopNotification\DesktopNotification')

def display_notification():
    icon_path = os.path.join(os.curdir, 'icon1.ico')
    notification.notify(
        title = "Please Drink Water Now!!", 
        message="The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women." , 
        app_icon = icon_path,  
                        # displaying time 
        timeout=10
        )
  
if __name__=="__main__":
     while True:
        display_notification()
        webbrowser.open("https://www.example.com/learn-about-hydration")  # Opens in the default browser
        
        time.sleep(1800)  # wait for 5 seconds before showing the notification again

        # Check if the user has entered something in the terminal
        # if input("Enter something to stop the notification: "):
        #     print("Thank you! The notification will now stop.")
        #     break
        
                

