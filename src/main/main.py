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

# from src.language.java import Java
from src.language.python import Python
from src.main.app import App
import pandas as pd

LANGUAGE = Python()
# remote_url = "https://github.com/pallets/flask.git"
# branch_name = "main"

def main(remote_url, branch_name, hashs):
    if not remote_url or not branch_name:
        raise ValueError("remote_url and branch_name must be provided")

    #App().collect_full_data(REMOTE_PATH, BRANCH, LANGUAGE)
    '''
    First execution mode.
    Collect all data.
    '''

    # hashs = ['859d9a9d5c3da114132ec9f0e515e1fa8030f68f']
    return App().collect_all_file_commit_subset(remote_url, branch_name, LANGUAGE, hashs)
    '''
    Second execution mode.
    Collect data only for specific commits.
    '''

    # files = ['app.py']
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

    df = pd.read_csv('./commits_ - commits_.csv')
    hashs = list(df['hash'])

    res = main("https://github.com/pallets/flask.git", "main", hashs)

    rows = []
    for commit_hash, commit_info in res.items():
        if 'files' not in commit_info.keys():
            continue
        for file_name, file_info in commit_info['files'].items():
            if 'hunks' not in file_info.keys():
                continue
            for idx_hunk, hunk in file_info['hunks'].items():
                row = {
                    "hash": commit_hash, 
                    "left_identifiers": [],
                    "right_identifiers": [],
                }
                if 'left_touched_elements' in hunk.keys():
                    for idx_element, element in hunk['left_touched_elements'].items():
                        if (element['identifier'] == 'try_statement' or 
                            element['identifier'] == 'else_clause' or 
                            element['identifier'] == 'except_clause' or 
                            element['identifier'] == 'finally_clause' or
                            element['identifier'] == 'raise_statement'):
                            row['left_identifiers'].append(element['identifier'])
                if 'right_touched_elements' in hunk.keys():
                    for idx_element, element in hunk['right_touched_elements'].items():
                        if (element['identifier'] == 'try_statement' or 
                            element['identifier'] == 'else_clause' or 
                            element['identifier'] == 'except_clause' or 
                            element['identifier'] == 'finally_clause' or
                            element['identifier'] == 'raise_statement'):
                            row['right_identifiers'].append(element['identifier'])
                
                if row['left_identifiers'] or row['right_identifiers']:
                    rows.append(row)
    dfout = pd.DataFrame(rows, columns=["hash", "left_identifiers", "right_identifiers"])    
    dfout.to_csv('./output/flask.csv')

