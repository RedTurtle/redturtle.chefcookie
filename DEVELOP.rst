Using the development buildout
==============================

Create a virtualenv in the package::

    $ virtualenv --clear .

Install requirements with pip::

    $ ./bin/pip install -r requirements.txt

Run buildout::

    $ ./bin/buildout

Start Plone in foreground:

    $ ./bin/instance fg


Running tests
-------------

    $ tox

list all tox environments:

    $ tox -l
    py27-Plone43
    py27-Plone51
    py27-Plone52
    py37-Plone52
    build_instance
    code-analysis
    lint-py27
    lint-py37
    coverage-report

run a specific tox env:

    $ tox -e py37-Plone52


Minified JS/CSS assets
-----------------------

``redturtle_chefcookie.js``, ``redturtle_chefcookie_tech.js`` and ``styles.css``
(under ``src/redturtle/chefcookie/browser/static/``) are shipped both as
readable sources and as minified files that are actually served to the
browser. If you edit one of those sources, regenerate the minified files
with (requires Node/npx, esbuild is fetched on the fly)::

    $ make minify

CI (``.github/workflows/minified-assets.yml``) runs ``make check-minified``,
which regenerates the minified files and fails if that produces a diff, to
catch a source edited without regenerating its ``.min`` counterpart.

