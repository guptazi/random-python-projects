import time
from plyer import notification

while True:
    notification.notify(
        title='Hello Notify',
        message=' Today is last day of assignment',
        timeout=10

    )
    time.sleep(10)