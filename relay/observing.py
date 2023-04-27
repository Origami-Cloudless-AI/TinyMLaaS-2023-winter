# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/observing.ipynb.

# %% auto 0
__all__ = ['read_person_detection_from_serial']

# %% ../nbs/observing.ipynb 1
import serial

# %% ../nbs/observing.ipynb 2
def read_person_detection_from_serial(port:str):
    "Reads a single person detection prediction line over serial and returns dict containing scores with keys `Person` and `No person`. Returns None if serial fails."
    try:
        with serial.Serial(port, 19200, timeout=1) as ser:
            output = ser.readline().decode("ascii").strip() # "Person score: 60.54% No person score: 39.45%"
            parts = output.split(" ")
            return {"Person":float(parts[2][:-1]), "No person":float(parts[6][:-1])}
    except:
        return None
