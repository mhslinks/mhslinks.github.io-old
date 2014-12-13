MHS Links
========

A collection of links (and more) for Melbourne High School. Currently contains various links to useful websites, as well as a collection of staff Edumail email links.

MHS Links is generated using a Python script using the [Jinja2](http://jinja.pocoo.org/) templating system using data from `/data/`. Extending the website is as simple as adding a new row to a CSV.


Live sites
========

* http://mhslinks.tumblr.com/ (generated to `/generated/tumblr/`)
* http://mc.powered.technology/mhs/ (generated to `/generated/standalone/`)


Generating the HTML
========

Prerequisites:
* [Python](https://www.python.org/downloads/) **2**
* [Jinja2](http://jinja.pocoo.org/)

If you wish to install Jinja2 on your system, I would personally recommend you use `pip` ([installation instructions](https://pip.pypa.io/en/latest/installing.html)) to install. Run `pip install jinja2` and you should be set.

After all the prerequisites have been met, simply run `python generate.py` and the pages will be generated to `/generated/`.

Tumblr
========

If you wish to configure a Tumblr version of this site, there is some configuration needed for it to work. Documentation of this is currently a work in progress.


Contributing
========

**PLEASE NOTE** that the emails are automatically sorted alphabetically by the template so there is no need to manually sort it in the CSV.

Anyone can feel free to contribute to MHS Links, whether it be the addition of new links or new emails. Please send a pull request and I will update both live sites.