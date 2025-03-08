import pytest
from adventure import Adventurer, Goblin, TreasureChest  # Assuming student's code is in adventure.py


def test_treasure_chest_class_exists(): #7
    """Test that the TreasureChest class is defined."""
    assert "TreasureChest" in globals(), "TreasureChest class not defined"

def test_treasure_chest_constructor(): #7
    """Test TreasureChest constructor initializes attributes correctly."""
    chest = TreasureChest(items=["Potion", "Arrows"])
    assert chest.items == ["Potion", "Arrows"], "TreasureChest items not initialized correctly"
    assert chest.is_open == False, "TreasureChest is_open not initialized to False"

