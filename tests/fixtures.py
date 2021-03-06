import os
import pytest
import calendar
import time

@pytest.fixture
def tmp_dat_file(tmpdir):
    ts = calendar.timegm(time.gmtime())
    filepath = os.path.join(tmpdir.dirname, str(ts) + "_tmp.dat")
    file = open(filepath, "w")
    file.close()
    yield filepath

