#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2020
month = 12
day = 1
hour = 0
minute = 0

def test_code():
    assert 0 > 1, "error"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day, hour + 6, minute), "Submitted Late"
