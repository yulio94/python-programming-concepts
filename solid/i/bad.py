class UnderlingInterface:
    def program(self):
        """"""

    def filetps(self):
        """"""

    def collate(self):
        """"""


class Underling(UnderlingInterface):
    def program(self):
        return 'Program initech systems to deposit fractions of pennies to private account';

    def filetps(self):
        return 'Place cover sheet on TPS report before going out';

    def collate(self):
        return 'Collect and combine texts, information, and figures in proper order.';


class Consultant(UnderlingInterface):

    def program(self):
        return 'Outsource task to India'

    def filetps(self):
        return 'Place cover sheet on TPS report before going out';

    def collate(self):
        return None


class Lumbergh:
    underling = None

    def __construct(self, UnderlingInterface, underling):
        underling = underling

    def harass(self):
        underling = program()
        underling = filetps()
        underling = collate()
