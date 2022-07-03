""" Main module.

To compute data about a target Git repository, the user must set the following constants:
- LANGUAGE: <Java() or Python()>. This constant indicates the language of the source code in the target repository.
- REPOSITORY_REMOTE_PATH: <https://github.com/user/repo.git>. This constant indicates the remote path of the target repository.
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

    #COMMIT = ['2a27d09a1716a1a0bc73101fb0a8a864996cd005']
    #App().collect_commit_subset(REMOTE_PATH, BRANCH, LANGUAGE, COMMIT)
    '''
    Second execution mode.
    Collect data only for specific commits.
    '''

    FILE = ['Calculator.java']
    #App().collect_file_subset(REMOTE_PATH, BRANCH, LANGUAGE, FILE)
    '''
    Third execution mode.
    Collect data only for specific files.
    '''

    COMMIT = '2a27d09a1716a1a0bc73101fb0a8a864996cd005'
    FILE = 'src/test/java/com/thealgorithms/maths/PascalTriangleTest.java'
    App().collect_file_commit(REMOTE_PATH, BRANCH, LANGUAGE, COMMIT, FILE)
    '''
    Fourth execution mode.
    Collect data for one file in one commit.
    '''
if __name__ == "__main__":
    main()