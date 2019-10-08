


class Contact:
    def __init__(self, id=None, firstname=None, lastname=None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):
        return "%s:%s;%s" % (self.id, self.firstname, self.lastname)