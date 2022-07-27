#!/usr/bin/env python

"""Tests for `mesh_sql` package."""

import unittest
from mesh_sql.database import database_connect


class TestTemplate(unittest.TestCase):
    """Tests for `mesh_sql` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test if database can start."""
        assert database_connect.start_db
