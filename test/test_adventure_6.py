import pytest
from adventure import Adventurer, Goblin, TreasureChest  # Assuming student's code is in adventure.py

def test_goblin_class_exists(): #6
    """Test that the Goblin class is defined."""
    assert "Goblin" in globals(), "Goblin class not defined"

def test_goblin_constructor(): #6
    """Test Goblin constructor initializes attributes correctly."""
    goblin = Goblin(name="TestGoblin", initial_health=40, attack_power=20)
    assert goblin.name == "TestGoblin", "Goblin name not initialized correctly"
    assert goblin.health == 40, "Goblin health not initialized correctly"
    assert goblin.attack_power == 20, "Goblin attack_power not initialized correctly"

def test_goblin_make_sound(): #6
    """Test Goblin make_sound method returns correct sound."""
    goblin = Goblin(name="SoundGoblin", initial_health=30, attack_power=15)
    sound = goblin.make_sound()
    assert sound == "Hehehe!", "Goblin make_sound returned incorrect sound"

def test_goblin_take_damage(): #6
    """Test Goblin take_damage method reduces health correctly."""
    goblin = Goblin(name="DamageGoblin", initial_health=50)
    goblin.take_damage(20)
    assert goblin.health == 30, "Goblin health not reduced correctly"
    goblin.take_damage(60) # Should not go below zero
    assert goblin.health == 0, "Goblin health went below zero"
