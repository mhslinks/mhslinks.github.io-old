PLEASE NOTE: This version of MHS Links is now deprecated for the newer [MHS Links](https://github.com/mhslinks/mhslinks.github.io) generated using Jekyll. Please submit pull requests to that repo, not this one.

MHS Links (old)
========

A collection of links (and more) for Melbourne High School. Currently contains various links to useful websites, as well as a collection of staff Edumail email links.

MHS Links is generated using a Python script using the [Jinja2](http://jinja.pocoo.org/) templating system using data from `/data/`. Most of the data comes from `.csv` files found in `/data/csv/`.


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

Anyone can feel free to contribute to MHS Links, whether it be the addition of new links or new emails. Note that the emails are automatically sorted, so there is no need to manually sort it in the CSV.

For most people, the easiest way is to privately message me over a medium such as Facebook. If you know the ropes of `git` and GitHub, please send a pull request or make an issue.
