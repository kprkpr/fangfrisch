"""
Copyright © 2020 Ralph Seichter

This file is part of "Fangfrisch".

Fangfrisch is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Fangfrisch is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar. If not, see <https://www.gnu.org/licenses/>.
"""
import logging
import unittest
import uuid

from fangfrisch.logging import log


def to_bool(x: str) -> bool:
    return x and x.lower() in ['1', 'enabled', 'y', 'yes', 'true']


class FangfrischTest(unittest.TestCase):
    CONF = 'tests/tests.conf'
    TMPDIR = f'/tmp/fangfrisch/unittest'
    UNITTEST = 'unittest'
    UNKNOWN = uuid.uuid4().hex

    @classmethod
    def setUpClass(cls) -> None:
        log.setLevel(logging.FATAL)
