import os
from sphinx import application

BASE_CONF = """\
import sys
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
sys.path.append('ext')
extensions = ['ext.lpblock']
master_doc = 'index'
nitpicky = True
"""

INDEX = """\
=====
PyLiT
=====

..  toctree::
    :maxdepth: 2

..  pylit:file::    test.py
    :language: python

..  pylit_block_list::
"""

def main():
    with open('conf.py','w') as f:
        f.write(BASE_CONF)
    with open('index.rst','w') as f:
        f.write(INDEX)

    srcdir = confdir = '.'
    outdir = './_build/html'
    doctreedir = './_build/doctrees'

    app = application.Sphinx(srcdir,confdir, outdir, doctreedir, 'html')
    app.builder.build_all()
    html_body = open(outdir + '/index.html').read()
    print(html_body)

if __name__ == '__main__':
    main()

