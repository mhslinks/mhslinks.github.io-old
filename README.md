MHS Links
========

A collection of links (and more) for Melbourne High School. Currently contains various links to useful websites, as well as a collection of staff Edumail email links.

MHS Links is generated using a Python script using the [Jinja2](http://jinja.pocoo.org/) templating system using data from `/data/`. Extending the website is as simple as adding a new row to a CSV.


Live sites
========

* http://mhslinks.github.io/ (using the same HTML as the above)

In the past, this was running on Tumblr, then mc.powered.technology, then mcpower.github.io. However, supporting so many sites was tedious and confusing for users. Everything has then moved to this repo here.


Generating the HTML
========

Prerequisites:
* [Python](https://www.python.org/downloads/) **2** (Jinja2 does not fully support Python 3 at the moment, unfortunately)
* [Jinja2](http://jinja.pocoo.org/)

If you wish to install Jinja2 on your system, I would personally recommend you use `pip` ([installation instructions](https://pip.pypa.io/en/latest/installing.html)) to install. Run `pip install jinja2` and you should be set.

After all the prerequisites have been met, simply run `python generate.py` and the pages will be generated to `/generated/`.


Contributing
========

**PLEASE NOTE** that the emails are automatically sorted alphabetically by the template so there is no need to manually sort it in the CSV.

Anyone can feel free to contribute to MHS Links, whether it be the addition of new links or new emails. Please send a pull request and I will update both live sites.