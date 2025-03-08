import pytest
from adventure import Adventurer, Goblin, TreasureChest  # Assuming student's code is in adventure.py

def test_adventurer_class_exists(): #4
    """Test that the Adventurer class is defined."""
    assert "Adventurer" in globals(), "Adventurer class not defined"

def test_adventurer_constructor(): #4
    """Test Adventurer constructor initializes attributes correctly."""
    hero = Adventurer(name="TestHero", initial_health=150)
    assert hero.name == "TestHero", "Adventurer name not initialized correctly"
    assert hero.health == 150, "Adventurer health not initialized correctly"
    assert hero.inventory == {}, "Adventurer inventory not initialized as empty dictionary"

def test_adventurer_display_status(capsys): #4
    """Test Adventurer display_status method output."""
    hero = Adventurer(name="StatusHero", initial_health=75)
    hero.take_item("Sword")
    hero.take_item("Potion", quantity=3)
    hero.display_status()
    captured = capsys.readouterr()
    expected_output = """Adventurer Status:
Name:  StatusHero
Health: 75
Inventory: {'Sword': 1, 'Potion': 3}
"""
    assert captured.out == expected_output, "Adventurer display_status output incorrect"
