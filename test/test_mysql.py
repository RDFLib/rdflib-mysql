import graph_case
import context_case
import unittest
from nose import SkipTest
from n3_2_case import testN3Store
from rdflib.graph import Graph

mysqlconfigString="user=gjh,password=50uthf0rk,host=localhost,db=test"

class MySQLGraphTestCase(graph_case.GraphTestCase):
    store_name = "MySQL"
    storetest = True
    configString = path = mysqlconfigString
    create = True
    identifier = "rdflib_test"

    def testGraphValue(self):
        raise SkipTest("GraphValue is a known issue.")

    def testStatementNode(self):
        raise SkipTest("Statement node not handled by AbstractSQLStore")

class MySQLContextTestCase(context_case.ContextTestCase):
    store_name = "MySQL"
    storetest = True
    path = configString = mysqlconfigString
    create = True
    identifier = "rdflib_test"

    def testLenInMultipleContexts(self):
        raise SkipTest("Multiple contexts - known issue.")

class MySQLStoreTests(unittest.TestCase):
    storetest = True
    store_name = "MySQL"
    path = configString = mysqlconfigString
    create = True
    identifier = "rdflib_test"

    def setUp(self):
        self.graph = Graph(store=self.store_name)
        self.graph.destroy(self.path)
        self.graph.open(self.path, create=self.create)

    def tearDown(self):
        self.graph.destroy(self.path)
        self.graph.close()

    def test_MySQL_testN3_store(self):
        # raise SkipTest("Known issue")
        testN3Store('MySQL',self.configString)


MySQLGraphTestCase.storetest = True
MySQLContextTestCase.storetest = True
MySQLStoreTests.storetest = True

# To enable profiling data, use nose's built-in hookup with hotshot:
# nosetests --with-profile --profile-stats-file stats.pf test/test_mysql
# Also see Tarek Ziade's gprof2dot explorations:
# http://tarekziade.wordpress.com/2008/08/25/visual-profiling-with-nose-and-gprof2dot/

