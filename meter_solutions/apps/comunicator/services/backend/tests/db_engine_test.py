import os
import unittest
from unittest import mock

from loguru import logger

from apps.comunicator.services.backend.db_engine import save_to_database


class DBEngineTest(unittest.TestCase):
    @mock.patch.dict(os.environ, {"DATABASE_URL": "postgres://zatnprhbqigyrr:e7f7f780c32e99d316aa70d21b8676f995e5853d55b678a622dee370c08f4fa2@ec2-54-247-122-209.eu-west-1.compute.amazonaws.com:5432/d5pelk4p8drf4b"})
    def test_connection(self):

        indications = ' {"consumedEnergy": 6.01, ' \
                      '"voltage": 233.0, ' \
                      '"current": 0.0, ' \
                      '"frequency": 50.0, ' \
                      '"activePower": 0.0, ' \
                      '"reactivePower": 0.0, ' \
                      '"apparentPower": 0.0, ' \
                      '"powerFactor": 100.0}'
        save_to_database(indications, "GJVSD123HDS32")

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
