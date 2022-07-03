""" Definitions file.

Sets constants.

 __author__ = "João Correia"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "João Correia"
 __email__ = "jcorreia@inf.puc-rio.inf.br"
 __status__ = "Production"
"""

import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = ROOT_DIR.rsplit("/", 1)[0] + "/output/"
