"""Interface segregation principle"""

from .interfaces import (Filetpstable, Programable, Collatable)


class Underling(Programable, Filetpstable, Collatable):
    def program(self):
        return 'Program initech systems to deposit fractions of pennies to private account';

    def filetps(self):
        return 'Place cover sheet on TPS report before going out';

    def collate(self):
        return 'Collect and combine texts, information, and figures in proper order.';


class Consultant(Programable, Filetpstable):

    def program(self):
        return 'Outsource task to India'

    def filetps(self):
        return 'Place cover sheet on TPS report before going out';


class Lumbergh:

    def __construct(self, program: Programable, filetps: Filetpstable, collate: Collatable):
        self.program = program
        self.filetps = filetps
        self.collate = collate

    def harass(self):
        self.program.program()
        self.filetps.filetps()
        self.collate.collate()
