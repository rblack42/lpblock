from sphinx.domains.std import StandardDomain
from .PylitFileBlock import PylitFileBlock
from .PylitCodeBlock import PylitCodeBlock
from .PylitAddBlock import PylitAddBlock
from .PylitShellBlock import PylitShellBlock


class PylitDomain(StandardDomain):
    name = 'pylit'
    label = 'Pylit Block'

    directives = {
        'file': PylitFileBlock,
        'code': PylitCodeBlock,
        'add': PylitAddBlock,
        'shell': PylitShellBlock
    }
