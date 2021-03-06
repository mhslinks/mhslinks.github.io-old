import csv
from jinja2 import Environment, FileSystemLoader
import os
import os.path
import shutil
get_path = lambda x: os.path.join(os.path.dirname(__file__), x)
csv_location = get_path("data/csv")
txt_location = get_path("data/txt")


# Loads data from /data/ to the variable "data".
# CSVs get loaded as arrays of dicts, TXTs get loaded as strings.
# "data" is initialised with a timestamp.
data = {}


for (dirpath, dirnames, filenames) in os.walk(csv_location):
	csvs = filenames
	break
for (dirpath, dirnames, filenames) in os.walk(txt_location):
	txts = filenames
	break

for sheet in csvs:
	data[sheet[:-4]] = list(csv.DictReader(open(csv_location + "/" + sheet)))
for txt in txts:
	data[txt[:-4]] = open(txt_location + "/" + txt).read().rstrip()

env = Environment(loader=FileSystemLoader(get_path("templates")), trim_blocks=True, lstrip_blocks=True)

def generate_template(template_name, destination):
	generated = env.get_template(template_name).render(**data)
	destination = get_path(destination)
	dirname = os.path.dirname(destination)
	if not os.path.exists(dirname):
		os.makedirs(dirname)
	with open(destination, "w") as to_write:
		to_write.write(generated.encode("utf-8"))
print "deleting old generated files"
shutil.rmtree(get_path("generated/"), True) # this seems dangerous!

print "copying static files"
shutil.copytree(get_path("static/"), get_path("generated/static/"))
for template in env.list_templates():
	# generating standalone pages
	if template == "base.html":
		# no need to generate a template for standalone
		continue
	print "generating standalone", template
	# if it's the index, generate it in the top directory.
	if template == "index.html":
		generate_template(template, "generated/index.html")
	else:
		generate_template(template, "generated/{0}/index.html".format(template[:-5]))