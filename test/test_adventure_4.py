# test_initialize_log.py
import pytest
import adventure
import os
import datetime

LOG_FILE = "test_adventure_log.txt"

def test_initialize_log_creates_file():
    adventure.initialize_log(LOG_FILE)
    assert os.path.exists(LOG_FILE)
    os.remove(LOG_FILE)

def test_initialize_log_writes_header():
    adventure.initialize_log(LOG_FILE)
    with open(LOG_FILE, 'r') as f:
        header_line = f.readline()
        assert header_line.startswith("Adventure Log Started: ")
    os.remove(LOG_FILE)

def test_initialize_log_prints_confirmation():
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    adventure.initialize_log(LOG_FILE)
    sys.stdout = sys.__stdout__
    assert f"Adventure log initialized in {LOG_FILE}\n" == capturedOutput.getvalue()
    os.remove(LOG_FILE)

def test_initialize_log_ioerror_handling(monkeypatch):
    def mock_open_error(*args, **kwargs):
        raise IOError("Mock IO Error")
    monkeypatch.setattr("builtins.open", mock_open_error)

    with pytest.raises(IOError) as excinfo:
        adventure.initialize_log(LOG_FILE)
    assert "Mock IO Error" in str(excinfo.value)

    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stderr = capturedOutput
    try:
        adventure.initialize_log(LOG_FILE)
    except IOError:
        pass # Exception is expected, already tested
    finally:
        sys.stderr = sys.__stderr__
    assert "Error initializing adventure log: Could not write to file." in capturedOutput.getvalue()

    if os.path.exists(LOG_FILE): # In case file creation happened before error
        os.remove(LOG_FILE)
