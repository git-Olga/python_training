import random
import string
from model.group import Group
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))