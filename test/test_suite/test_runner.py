from unittest import TestLoader, TestSuite, TextTestRunner
from test.individual_page_test.individual_home import MyStoreHomePage
from test.individual_page_test.individual_authentication import MyStoreAuthentication
from test.individual_page_test.individual_registration import MyStoreRegistration
from test.e2e.application_flow import Smoke
import testtools as testtools


if __name__ == "__main__":

    loader = TestLoader()
    # if you don't want to run some tests, comment them out
    suite = TestSuite((loader.loadTestsFromTestCase(Smoke)
                       # loader.loadTestsFromTestCase(MyStoreHomePage),
                       # loader.loadTestsFromTestCase(MyStoreAuthentication),
                       #loader.loadTestsFromTestCase(MyStoreRegistration)
                       ))

    # run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

    # run test parallel using concurrent_suite - better to use pytest xdist instead!
    # concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    # concurrent_suite.run(testtools.StreamResult())