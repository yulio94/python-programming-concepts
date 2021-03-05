class Programmer:
    def code(self):
        return 'coding'


class Tester:
    def test(self):
        return 'testing'


class ProjectManagement:
    def process(self, member):
        if isinstance(member, Programmer):
            member.code()
        elif isinstance(member, Tester):
            member.test()
        raise Exception('Invalid input member')
