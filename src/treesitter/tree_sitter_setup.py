""" Class for setup the Tree Sitter.

Setup the Tree Sitter (https://tree-sitter.github.io/tree-sitter/) to support the target languages.

 __author__ = "João Correia"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "João Correia"
 __email__ = "jcorreia@inf.puc-rio.inf.br"
 __status__ = "Production"
"""

import os

from src.language.java import Java
from src.language.language import Language
from src.language.python import Python
from tree_sitter import Language as LanguageTreeSitter
from tree_sitter import Parser


class TreeSetup():

  def __init__(self, language: Language, lib_root_dir=os.path.join(os.getcwd(), 'src')):
    """
    Construct a new TreeSetup object, besides initialize the Tree Sitter for the target language.

    :param language: The Language object, defining the target language to be parsed.
    :return: Returns nothing.
    """

    paths = []

    if os.path.exists(os.path.join(lib_root_dir, 'tree-sitter-java')):
      paths.append(os.path.join(lib_root_dir, 'tree-sitter-java'))
    if os.path.exists(os.path.join(lib_root_dir, 'tree-sitter-python')):
      paths.append(os.path.join(lib_root_dir, 'tree-sitter-python'))

    LanguageTreeSitter.build_library(
      # Store the library in the `src` directory
      lib_root_dir + 'my-languages.so',
      paths
    )


    self.__language = language
    if isinstance(self.__language, Java):
      self.JAVA_LANGUAGE = LanguageTreeSitter(lib_root_dir + 'my-languages.so', 'java')
    elif isinstance(self.__language, Python):
      self.PY_LANGUAGE = LanguageTreeSitter(lib_root_dir + 'my-languages.so', 'python')


  def parser(self):
    """
    Constructs the Tree Sitter parser for the language.

    :return: The parser for the language.
    """
    parser = Parser()
    if isinstance(self.__language, Java):
      parser.set_language(self.JAVA_LANGUAGE)
    elif isinstance(self.__language, Python):
      parser.set_language(self.PY_LANGUAGE)

    return parser

