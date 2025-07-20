# test_shieldguard.py
"""
Tests for ShieldGuard module.
"""

import unittest
from shieldguard import ShieldGuard

class TestShieldGuard(unittest.TestCase):
    """Test cases for ShieldGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ShieldGuard()
        self.assertIsInstance(instance, ShieldGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ShieldGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
