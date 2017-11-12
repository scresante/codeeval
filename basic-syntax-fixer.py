#!/usr/bin/python3

#" for reformatting codeeval in vim
# nnoremap fv <Esc>:%s/f = argv/FILE = argv/<CR>
# :%s/f = 'test/FILE = 'test/<CR>
# :%s/data = open(f,/DATA = open(FILE, /<CR>
# :3,9s/except/except NameError/<CR>
# :%s/for line in data/for line in DATA/<CR>
# :let g:pymode_lint=0<CR>
# :let g:pymode_lint_on_write=0<CR>
# :let g:pymode_rope=0<CR>
from os import listdir
import re
FILELIST = listdir('.')
PYTHONFILES = list(filter(lambda x: (x.endswith('.py3') or x.endswith('.py2')),
                     FILELIST))
# REGEX = re.compile(r"""#!/usr/bin/python(.)
# from sys import import argv
# try:
  # f = argv[1]
# except:
  # f = 'tests/(\w*)'
# data = open(f,'r').read().splitlines()""", re.VERBOSE)

