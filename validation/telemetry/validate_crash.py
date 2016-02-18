import json, os, unittest
from jsonschema import validate, ValidationError

LOCAL = os.path.dirname(__file__)
SAMPLE_PINGS_PATH = '/Users/spenrose/fhrv4/crash-pings-100-sanitized.json'
CRASH_SCHEMA_PATH = os.path.join(LOCAL, '../../telemetry/crash.schema.json')


class Test_validate(unittest.TestCase):

    def setUp(self):
        with open(SAMPLE_PINGS_PATH) as f:
            self.pings = json.load(f)

    def test_crash(self):
        with open(CRASH_SCHEMA_PATH) as f:
            crash_schema = json.load(f)
        # The presence of $schema means that validate() will test
        # for specific JSON-Schema features
        self.failUnless("$schema" in crash_schema)
        # Sanity
        self.failUnless("properties" in crash_schema)
        for ping in self.pings:
            validate(ping, crash_schema)


if __name__ == '__main__':
    unittest.main()
