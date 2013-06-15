import sys
import unittest

import ut_track

loader = unittest.TestLoader()
suite = loader.loadTestsFromModule(ut_track)
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)