import logging

from django.http import request
from django.test import TestCase, tag
import app1.views


class YourTestClass(TestCase):
    @tag('log1')
    def test_logging(self):
        with self.assertLogs() as captured:
            app1.views.main(request=request)
        self.assertEqual(len(captured.records), 4)
        self.assertEqual(captured.records[0].getMessage(), "logger1 - debug")