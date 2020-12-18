from configparser import ConfigParser
from os import path
import json

PROJECT_DIR = path.abspath(path.dirname(path.dirname(__file__)))
CONF_FILE_DIR = path.join(PROJECT_DIR, 'menu', 'config.cfg')

parser = ConfigParser()
parser.read(CONF_FILE_DIR)

CONFIGTYPE_DICT = json.loads(parser.get('menu', 'configtype_dict'))
CHOICE_LIST = parser.get('main_build_choices', 'choice_list').strip('"').split(', ')
CONFIG_DIR_LIST = [elem + '_build' for elem in CHOICE_LIST]
CHOICE_NUM = len(CHOICE_LIST)
CONFIGTYPE_LIST = [CONFIGTYPE_DICT[elem] for elem in CONFIGTYPE_DICT]
MAIN_CHOICE = [key for key in CONFIGTYPE_DICT]

def test():
    print("PROJECT_DIR", PROJECT_DIR)
    print("CONF_FILE_DIR:", CONF_FILE_DIR)
    print('CONFIGTYPE_DICT:', CONFIGTYPE_DICT)
    print('CHOICE_LIST:', CHOICE_LIST)
    print("CONFIG_DIR_LIST:", CONFIG_DIR_LIST)
    print("CHOICE_NUM:", CHOICE_NUM)
    print("CONFIGTYPE_LIST:", CONFIGTYPE_LIST)
    print("MAIN_CHOICE", MAIN_CHOICE)

if __name__ == '__main__':
    test()