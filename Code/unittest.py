import coverage

cov = coverage.Coverage()
cov.start()

import test

cov.stop()
cov.save()

cov.html_report()