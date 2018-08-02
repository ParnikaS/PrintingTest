# tests/runner.py
import unittest

# import your test modules
import TestPrintMetaApi
import TestPrintingApi


# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(TestPrintMetaApi))
suite.addTests(loader.loadTestsFromModule(TestPrintingApi))
print(suite.countTestCases())

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)