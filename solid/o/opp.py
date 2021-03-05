"""Open/Closed principle"""

from .interfaces import Workable


class Programmer(Workable):

    def code(self):
        """"""
        return 'coding'

    def process(self):
        """"""
        self.code()


class Tester(Workable):

    def test(self):
        """"""
        return 'testing'

    def process(self):
        """"""
        self.test()


class ProjectManagement:
    """"""

    def process(self, member: Workable):
        """"""
        member.process()
