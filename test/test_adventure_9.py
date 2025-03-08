import pytest
from adventure import Adventurer, Goblin, TreasureChest  # Assuming student's code is in adventure.py


def test_treasure_chest_open_empty_chest(capsys): #9
    """Test TreasureChest open_chest method with empty chest."""
    hero = Adventurer(name="EmptyChestHero", initial_health=100)
    chest = TreasureChest(items=[]) # Empty chest
    open_result = chest.open_chest(hero)
    captured = capsys.readouterr()

    assert chest.is_open == True, "Empty TreasureChest is_open not set to True after opening"
    assert hero.inventory == {}, "Empty TreasureChest added items to adventurer's inventory (should be empty)"
    expected_empty_chest_output = "You open the chest, but it is empty."
    assert open_result == expected_empty_chest_output, f"open_chest return message for empty chest incorrect, got: '{open_result}', expected: '{expected_empty_chest_output}'"
