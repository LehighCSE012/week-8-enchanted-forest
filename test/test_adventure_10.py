import pytest
from adventure import Adventurer, Goblin, TreasureChest  # Assuming student's code is in adventure.py

def test_treasure_chest_is_chest_open(): #10
    """Test TreasureChest is_chest_open method."""
    chest = TreasureChest(items=["Potion"])
    assert chest.is_chest_open() == False, "is_chest_open returns True for a closed chest"
    chest.open_chest(Adventurer(name="Test", initial_health=100)) # Open the chest
    assert chest.is_chest_open() == True, "is_chest_open returns False for an open chest"
