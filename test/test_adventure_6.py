# test_load_inventory.py
import pytest
import adventure
import os
import json

INVENTORY_FILE = "test_inventory.json"

def teardown_module():
    if os.path.exists(INVENTORY_FILE):
        os.remove(INVENTORY_FILE)

def test_load_inventory_existing_file():
    test_inventory_data = {"Potion": 3, "Gold": 10}
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(test_inventory_data, f)

    loaded_inventory = adventure.load_inventory(INVENTORY_FILE)
    assert loaded_inventory == test_inventory_data

def test_load_inventory_non_existent_file():
    if os.path.exists(INVENTORY_FILE):
        os.remove(INVENTORY_FILE)

    loaded_inventory = adventure.load_inventory(INVENTORY_FILE)
    assert loaded_inventory == {}

    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    adventure.load_inventory(INVENTORY_FILE)
    sys.stdout = sys.__stdout__
    assert f"Inventory file not found. Creating a new one: {INVENTORY_FILE}\n" == capturedOutput.getvalue()

def test_load_inventory_invalid_json():
    with open(INVENTORY_FILE, 'w') as f:
        f.write("invalid json data")

    loaded_inventory = adventure.load_inventory(INVENTORY_FILE)
    assert loaded_inventory == {}

    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stderr = capturedOutput
    adventure.load_inventory(INVENTORY_FILE)
    sys.stderr = sys.__stderr__
    assert "Error loading inventory: Invalid JSON format. Starting with an empty inventory." in capturedOutput.getvalue()

def test_load_inventory_ioerror_handling(monkeypatch):
    def mock_open_error(*args, **kwargs):
        raise IOError("Mock IO Error")
    monkeypatch.setattr("builtins.open", mock_open_error)

    with pytest.raises(IOError) as excinfo:
        adventure.load_inventory(INVENTORY_FILE)
    assert "Mock IO Error" in str(excinfo.value)

    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stderr = capturedOutput
    try:
        adventure.load_inventory(INVENTORY_FILE)
    except IOError:
        pass # Exception is expected, already tested
    finally:
        sys.stderr = sys.__stderr__
    assert "Error loading inventory: Could not read inventory file." in capturedOutput.getvalue()
