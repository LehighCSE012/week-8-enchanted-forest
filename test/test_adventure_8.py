# test_add_item_to_inventory.py
import pytest
import adventure

def test_add_item_to_empty_inventory():
    inventory = {}
    adventure.add_item_to_inventory(inventory, "Potion")
    assert inventory == {"Potion": 1}

def test_add_item_to_non_empty_inventory():
    inventory = {"Potion": 1}
    adventure.add_item_to_inventory(inventory, "Torch")
    assert inventory == {"Potion": 1, "Torch": 1}

def test_add_existing_item_increase_quantity():
    inventory = {"Potion": 2}
    adventure.add_item_to_inventory(inventory, "Potion", 3)
    assert inventory == {"Potion": 5}

def test_add_item_default_quantity():
    inventory = {}
    adventure.add_item_to_inventory(inventory, "Gold")
    assert inventory == {"Gold": 1}

def test_add_item_prints_confirmation():
    inventory = {}
    item_name = "Sword"
    quantity = 2
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    adventure.add_item_to_inventory(inventory, item_name, quantity)
    sys.stdout = sys.__stdout__
    assert f"Added {quantity} {item_name}(s) to inventory.\n" == capturedOutput.getvalue()
    assert inventory == {"Sword": 2}

def test_add_item_prints_confirmation_singular():
    inventory = {}
    item_name = "Potion"
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    adventure.add_item_to_inventory(inventory, item_name)
    sys.stdout = sys.__stdout__
    assert f"Added 1 {item_name} to inventory.\n" == capturedOutput.getvalue()
    assert inventory == {"Potion": 1}
