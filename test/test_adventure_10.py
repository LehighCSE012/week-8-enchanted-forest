# test_main_adventure_flow.py
import pytest
import adventure
import os
import json
import datetime
from unittest.mock import patch

LOG_FILE = "test_adventure_log.txt"
INVENTORY_FILE = "test_inventory.json"

def setup_module():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    if os.path.exists(INVENTORY_FILE):
        os.remove(INVENTORY_FILE)

def teardown_module():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    if os.path.exists(INVENTORY_FILE):
        os.remove(INVENTORY_FILE)

def test_main_function_runs_without_error():
    with patch('builtins.input', return_value="left"): # Mock input for 'left' choice
        adventure.main(LOG_FILE, INVENTORY_FILE)

def test_main_log_initialization():
    with patch('builtins.input', return_value="left"):
        adventure.main(LOG_FILE, INVENTORY_FILE)
    assert os.path.exists(LOG_FILE)
    with open(LOG_FILE, 'r') as f:
        log_content = f.read()
        assert "Adventure Log Started:" in log_content
        assert "Adventurer enters the Caves of Orzammar." in log_content

def test_main_inventory_load_and_save():
    initial_inventory = {"Potion": 1}
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(initial_inventory, f)

    with patch('builtins.input', return_value="right"):
        adventure.main(LOG_FILE, INVENTORY_FILE)

    assert os.path.exists(INVENTORY_FILE)
    with open(INVENTORY_FILE, 'r') as f:
        saved_inventory = json.load(f)
        assert "Torch" in saved_inventory # 'right' path adds Torch
        assert "Potion" in saved_inventory # Initial item preserved

def test_main_left_path_flow():
    with patch('builtins.input', return_value="left"):
        adventure.main(LOG_FILE, INVENTORY_FILE)

    with open(LOG_FILE, 'r') as f:
        log_content = f.read()
        assert "Adventurer chose to go left." in log_content
        assert "Found Rusty Sword." in log_content
        assert "Found Potion." in log_content
        assert "Inventory saved before exiting caves." in log_content
        assert "Adventurer exits the Caves of Orzammar." in log_content

    with open(INVENTORY_FILE, 'r') as f:
        saved_inventory = json.load(f)
        assert "Rusty Sword" in saved_inventory
        assert "Potion" in saved_inventory

def test_main_right_path_flow():
    with patch('builtins.input', return_value="right"):
        adventure.main(LOG_FILE, INVENTORY_FILE)

    with open(LOG_FILE, 'r') as f:
        log_content = f.read()
        assert "Adventurer chose to go right." in log_content
        assert "Found Torch." in log_content
        assert "Inventory saved before exiting caves." in log_content
        assert "Adventurer exits the Caves of Orzammar." in log_content
        assert "Found a hidden passage with a riddle:" in log_content # Check for clue log

    with open(INVENTORY_FILE, 'r') as f:
        saved_inventory = json.load(f)
        assert "Torch" in saved_inventory

def test_main_invalid_input_flow(monkeypatch):
    inputs = iter(["invalid", "left"]) # First invalid, then valid 'left'
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    adventure.main(LOG_FILE, INVENTORY_FILE)

    with open(LOG_FILE, 'r') as f:
        log_content = f.read()
        assert "Invalid direction input received." in log_content
        assert "Adventurer chose to go left." in log_content # Should proceed after valid input
