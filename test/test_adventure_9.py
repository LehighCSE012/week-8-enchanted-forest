# test_display_inventory.py
import pytest
import adventure
import io
import sys

def capture_stdout(func, *args, **kwargs):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    func(*args, **kwargs)
    sys.stdout = sys.__stdout__
    return capturedOutput.getvalue()

def test_display_inventory_empty():
    inventory = {}
    output = capture_stdout(adventure.display_inventory, inventory)
    assert output == "Inventory is empty.\n"

def test_display_inventory_non_empty():
    inventory = {"Potion": 2, "Torch": 1, "Gold Coins": 50}
    output = capture_stdout(adventure.display_inventory, inventory)
    expected_output_lines = [
        "Current Inventory:",
        " - Potion: 2",
        " - Torch: 1",
        " - Gold Coins: 50",
        "" # newline at the end
    ]
    expected_output = "\n".join(expected_output_lines)
    assert output == expected_output

def test_display_inventory_single_item():
    inventory = {"Sword": 1}
    output = capture_stdout(adventure.display_inventory, inventory)
    expected_output_lines = [
        "Current Inventory:",
        " - Sword: 1",
        ""
    ]
    expected_output = "\n".join(expected_output_lines)
    assert output == expected_output
