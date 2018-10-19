from unittest import TestLoader, TestSuite, TextTestRunner
from test.e2e.application_flow import Smoke
import testtools as testtools


if __name__ == "__main__":

    loader = TestLoader()
    # if you don't want to run some tests, comment them out
    suite = TestSuite((loader.loadTestsFromTestCase(Smoke)))

    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

    # run test parallel using concurrent_suite - better to use pytest xdist instead!
    # concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    # concurrent_suite.run(testtools.StreamResult())