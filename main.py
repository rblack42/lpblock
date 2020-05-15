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
    fout = open('conf.py','w')
    fout.write(BASE_CONF)
    fout.close()
    fout = open('index.rst','w')
    fout.write(INDEX)
    fout.close()

    srcdir = confdir = '.'
    outdir = './_build/html'
    doctreedir = './_build/doctrees'

    app = application.Sphinx(srcdir,confdir, outdir, doctreedir, 'html')
    app.builder.build_all()
    html_body = open(outdir + '/index.html').read()
    print(html_body)

if __name__ == '__main__':
    main()

