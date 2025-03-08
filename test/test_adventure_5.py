# test_log_entry.py
import pytest
import adventure
import os
import datetime
import time

LOG_FILE = "test_adventure_log.txt"

def setup_module():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    adventure.initialize_log(LOG_FILE)

def teardown_module():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

def test_log_entry_writes_entry():
    test_entry = "Test log entry"
    adventure.log_entry(LOG_FILE, test_entry)
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
        assert len(lines) > 1 # Header + at least one entry
        last_line = lines[-1]
        assert test_entry in last_line
        assert last_line.startswith("[") and last_line.split("]")[1].strip() == f"- {test_entry}"

def test_log_entry_timestamp_format():
    test_entry = "Timestamp format test"
    adventure.log_entry(LOG_FILE, test_entry)
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
        last_line = lines[-1]
        timestamp_str = last_line[1:20] # Extract timestamp part
        try:
            datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            pytest.fail("Timestamp is not in correct format")

def test_log_entry_append_mode():
    entry1 = "First entry"
    entry2 = "Second entry"
    adventure.log_entry(LOG_FILE, entry1)
    adventure.log_entry(LOG_FILE, entry2)
    with open(LOG_FILE, 'r') as f:
        lines = f.readlines()
        assert len(lines) >= 3 # Header + two entries
        assert entry1 in lines[-2]
        assert entry2 in lines[-1]

def test_log_entry_ioerror_handling(monkeypatch):
    def mock_open_error(*args, **kwargs):
        raise IOError("Mock IO Error")
    monkeypatch.setattr("builtins.open", mock_open_error)

    test_entry = "Entry causing error"
    with pytest.raises(IOError) as excinfo:
        adventure.log_entry(LOG_FILE, test_entry)
    assert "Mock IO Error" in str(excinfo.value)

    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stderr = capturedOutput
    try:
        adventure.log_entry(LOG_FILE, test_entry)
    except IOError:
        pass # Exception is expected, already tested
    finally:
        sys.stderr = sys.__stderr__
    assert "Error writing to adventure log: Could not write entry." in capturedOutput.getvalue()
