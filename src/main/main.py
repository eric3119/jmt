""" Main module.

To compute data about a target Git repository, the user must set the following constants:
- LANGUAGE: <Java() or Python()>. This constant indicates the language of the source code in the target repository.
- REMOTE_PATH: <https://github.com/user/repo.git>. This constant indicates the remote path of the target repository.
- BRANCH: <master>. This constant indicates the branch in the target repository that must be analysed.

 __author__ = "João Correia"
 __license__ = "GPL"
 __version__ = "1.0.0"
 __maintainer__ = "João Correia"
 __email__ = "jcorreia@inf.puc-rio.inf.br"
 __status__ = "Production"
"""

from src.language.java import Java
from src.language.python import Python
from src.main.app import App

LANGUAGE = Java()
REMOTE_PATH = "https://github.com/correiajoao/Java.git"
BRANCH = "master"

def main():

    #App().collect_full_data(REMOTE_PATH, BRANCH, LANGUAGE)
    '''
    First execution mode.
    Collect all data.
    '''

    #hashs = ['']
    App().collect_all_file_commit_subset(REMOTE_PATH, BRANCH, LANGUAGE, hashs)
    '''
    Second execution mode.
    Collect data only for specific commits.
    '''

    #files = ['']
    #App().collect_all_commit_file_subset(REMOTE_PATH, BRANCH, LANGUAGE, files)
    '''
    Third execution mode.
    Collect data only for specific files.
    '''

    #hashs = ['']
    #files = ['']
    #App().collect_one_file_one_commit(REMOTE_PATH, BRANCH, LANGUAGE, hashs, files)
    '''
    Fourth execution mode.
    Collect data for one file in one commit.
    '''
if __name__ == "__main__":
    main()