from datetime import datetime


def get_time():
    now = datetime.now()
    return now.strftime("%d/%m/%Y %H:%M:%S")