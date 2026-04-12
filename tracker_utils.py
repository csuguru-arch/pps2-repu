import time

def calculate_duration(start, end):
    return round(end - start, 2)

def format_time(seconds):
    minutes = seconds / 60
    return round(minutes, 2)
