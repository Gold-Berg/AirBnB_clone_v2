#!/usr/bin/python3
#!/usr/bin/python3
import unittest
import sys
import os
import json
import models
import pep8
from models.base_model import BaseModel
from io import StringIO
from console import HBNBCommand
from datetime import datetime
class TestConsole(unittest.TestCase):
    """Unit test class for HBNBCommand"""

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()
        sys.stdout = StringIO()

    def tearDown(self):
        """Tear down test environment"""
        sys.stdout = sys.__stdout__

    def test_create(self):
        """Test create command"""
        self.assertFalse(BaseModel.count())  # No instances before create
        self.console.onecmd("create BaseModel")
        self.assertTrue(BaseModel.count())  # Instance created

    def test_show(self):
        """Test show command"""
        new_instance = BaseModel()
        new_instance_id = new_instance.id
        self.console.onecmd("show BaseModel {}".format(new_instance_id))
        output = sys.stdout.getvalue().strip()
        self.assertIn(new_instance_id, output)  # Instance shown

    def test_destroy(self):
        """Test destroy command"""
        new_instance = BaseModel()
        new_instance_id = new_instance.id
        self.assertTrue(BaseModel.count())  # Instance created
        self.console.onecmd("destroy BaseModel {}".format(new_instance_id))
        self.assertFalse(BaseModel.count())  # Instance destroyed

    def test_all(self):
        """Test all command"""
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("all BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(len(output.split('\n')), 2)  # Correct output

    def test_count(self):
        """Test count command"""
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("create BaseModel")
        self.console.onecmd("count BaseModel")
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, '3')  # Correct count

    def test_update(self):
        """Test update command"""
        new_instance = BaseModel()
        new_instance_id = new_instance.id
        self.console.onecmd("update BaseModel {} name 'New Name'".format(new_instance_id))
        self.assertEqual(new_instance.name, 'New Name')  # Attribute updated


    def test_pep8(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["console.py"])
        self.assertEqual(result.total_errors, 0)

    def test_pep8_test_base_model(self):
        """Test that tests/test_models/test_base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(["tests/test_console.py"])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Constructor documentation"""
        doc = TestConsole.__init__.__doc__
        self.assertGreater(len(doc), 1)

if __name__ == "__main__":
    unittest.main()
