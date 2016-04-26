# If everything works this script should print:
#     Goto test
#     Hello
#     World!
#
from jygoto import goto
from jygoto import label

print "Goto test"

goto .my_label
print "Goodbye"
label .my_label
print "Hello"
print "World!"
