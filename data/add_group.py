from model.group import Group
import random
import string

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

def random_sring(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_sring("name", 10)]
#    for header in ["", random_sring("header", 20)]
#    for footer in ["", random_sring("footer", 20)]
#]


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_sring("name", 10), header=random_sring("header", 20), footer=random_sring("footer", 20))
    for i in range(5)
]