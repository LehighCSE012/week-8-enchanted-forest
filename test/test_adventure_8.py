import pytest
from adventure import Adventurer, Goblin, TreasureChest  # Assuming student's code is in adventure.py


def test_treasure_chest_open_chest(capsys): #8
    """Test TreasureChest open_chest method functionality."""
    hero = Adventurer(name="ChestHero", initial_health=100)
    chest = TreasureChest(items=["Magic Ring", "Arrows"])
    open_result = chest.open_chest(hero)
    captured = capsys.readouterr()

    assert chest.is_open == True, "TreasureChest is_open not set to True after opening"
    assert "Magic Ring" in hero.inventory and "Arrows" in hero.inventory, "open_chest did not add items to adventurer's inventory"
    expected_chest_output = "You open the chest and find: Magic Ring, Arrows."
    assert open_result == expected_chest_output, f"open_chest return message incorrect, got: '{open_result}', expected: '{expected_chest_output}'"

    # Test opening already opened chest
    open_result_again = chest.open_chest(hero)
    assert open_result_again == "The chest is already open.", "open_chest on already open chest returned incorrect message"

