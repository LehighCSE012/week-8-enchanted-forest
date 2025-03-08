# test_save_inventory.py
import pytest
import adventure
import os
import json

INVENTORY_FILE = "test_inventory.json"

def teardown_module():
    if os.path.exists(INVENTORY_FILE):
        os.remove(INVENTORY_FILE)

def test_save_inventory_writes_file():
    test_inventory_data = {"Potion": 2, "Torch": 1}
    adventure.save_inventory(INVENTORY_FILE, test_inventory_data)
    assert os.path.exists(INVENTORY_FILE)

def test_save_inventory_correct_json_format():
    test_inventory_data = {"Potion": 2, "Torch": 1}
    adventure.save_inventory(INVENTORY_FILE, test_inventory_data)
    with open(INVENTORY_FILE, 'r') as f:
        loaded_data = json.load(f)
        assert loaded_data == test_inventory_data

def test_save_inventory_pretty_formatting():
    test_inventory_data = {"Potion": 2, "Torch": 1}
    adventure.save_inventory(INVENTORY_FILE, test_inventory_data)
    with open(INVENTORY_FILE, 'r') as f:
        content = f.read()
        assert "    \"Potion\":" in content # Check for indent

def test_save_inventory_prints_confirmation():
    test_inventory_data = {"Potion": 2, "Torch": 1}
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    adventure.save_inventory(INVENTORY_FILE, test_inventory_data)
    sys.stdout = sys.__stdout__
    assert f"Inventory saved to {INVENTORY_FILE}\n" == capturedOutput.getvalue()

def test_save_inventory_ioerror_handling(monkeypatch):
    def mock_open_error(*args, **kwargs):
        raise IOError("Mock IO Error")
    monkeypatch.setattr("builtins.open", mock_open_error)

    test_inventory_data = {"Item": 1}
    with pytest.raises(IOError) as excinfo:
        adventure.save_inventory(INVENTORY_FILE, test_inventory_data)
    assert "Mock IO Error" in str(excinfo.value)

    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stderr = capturedOutput
    try:
        adventure.save_inventory(INVENTORY_FILE, test_inventory_data)
    except IOError:
        pass # Exception is expected, already tested
    finally:
        sys.stderr = sys.__stderr__
    assert "Error saving inventory: Could not write to file." in capturedOutput.getvalue()
