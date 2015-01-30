import csv
from jinja2 import Environment, FileSystemLoader
from os import walk
from time import localtime, strftime
import os.path
get_path = lambda x: os.path.join(os.path.dirname(__file__), x)
csv_location = get_path("data/csv")
txt_location = get_path("data/txt")


# Loads data from /data/ to the variable "data".
# CSVs get loaded as arrays of dicts, TXTs get loaded as strings.
# "data" is initialised with a timestamp.
data = {"timestamp": strftime("%a, %d %b %Y %H:%M:%S AEST", localtime())}


for (dirpath, dirnames, filenames) in walk(csv_location):
	csvs = filenames
	break
for (dirpath, dirnames, filenames) in walk(txt_location):
	txts = filenames
	break

for sheet in csvs:
	data[sheet[:-4]] = list(csv.DictReader(open(csv_location + "/" + sheet)))
for txt in txts:
	data[txt[:-4]] = open(txt_location + "/" + txt).read().rstrip()

env = Environment(loader=FileSystemLoader(get_path("templates")), trim_blocks=True, lstrip_blocks=True)

def generate_template(template_name, is_tumblr, destination):
	generated = env.get_template(template_name).render(tumblr=is_tumblr, **data)
	with open(get_path(destination), "w") as to_write:
		to_write.write(generated.encode("utf-8"))

for template in env.list_templates():
	# always generate a tumblr template for everything
	print "generating Tumblr", template
	generate_template(template, True, "generated/tumblr/{0}".format(template))

	# generating standalone pages
	if template == "base.html":
		# no need to generate a template for standalone
		continue
	print "generating standalone", template
	# if it's the index, generate it in the top directory.
	if template == "index.html":
		generate_template(template, False, "generated/standalone/index.html")
	else:
		generate_template(template, False, "generated/standalone/{0}/index.html".format(template[:-5]))