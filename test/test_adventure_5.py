import pytest
from adventure import Adventurer, Goblin, TreasureChest  # Assuming student's code is in adventure.py

def test_adventurer_take_damage(): #5
    """Test Adventurer take_damage method reduces health correctly."""
    hero = Adventurer(name="DamageHero", initial_health=100)
    hero.take_damage(30)
    assert hero.health == 70, "Adventurer health not reduced correctly"
    hero.take_damage(80) # Should not go below zero
    assert hero.health == 0, "Adventurer health went below zero"

def test_adventurer_take_item(): #5
    """Test Adventurer take_item method adds items to inventory."""
    hero = Adventurer(name="ItemHero", initial_health=100)
    hero.take_item("Gold Coins", quantity=50)
    assert hero.inventory == {"Gold Coins": 50}, "take_item failed to add new item"
    hero.take_item("Gold Coins", quantity=25)
    assert hero.inventory == {"Gold Coins": 75}, "take_item failed to increase existing item quantity"
    hero.take_item("Torch")
    assert hero.inventory == {"Gold Coins": 75, "Torch": 1}, "take_item failed to add different item"
