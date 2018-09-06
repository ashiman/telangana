from xpath_text import dump_text
import codecs
f = codecs.open("1.htm", 'r', "utf-8")
page = f.read()
dump = dump_text(page)
print dump