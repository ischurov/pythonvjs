# pythonvjs
This project is aimed to provide comprehensive side-by-side comparison of Python
and JavaScript syntax and language features.

The site is available [here](http://ischurov.github.io/pythonvjs).

If you want to contribute, you can edit files in the `source` directory. It's in
[qqmbr](http://github.com/ischurov/qqmbr) format, easy editable with
any text editor. Output of code samples is generated automatically (using
node.js for JS code).

To preview, run 

```
python pythonvjs.py
```

To build statis version, do

```
python freeze.py
```

Site generation uses [Flask](http://flask.pocoo.org) and to provide static
version we use [Frozen Flask](http://pythonhosted.org/Frozen-Flask/).
