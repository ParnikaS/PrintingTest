# tests/runner.py
import unittest

# import your test modules
import TestPrintMetaApi


# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTest(loader.loadTestsFromModule(TestPrintMetaApi))
print(suite.countTestCases())

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)