from configparser import ConfigParser
import logging
import os


def ensure_folder_existence(folders_path):
    """
    :input: folders_path: List
    """

    for folder_path in folders_path:
        existence = os.path.isdir(folder_path)
        if existence is False:
            os.mkdir(folder_path)


def get_config_data(path_file_config):
    """get default configuration data from file config.ini

    Returns:
        dict: config data
    """

    config_file = ConfigParser()
    config_file.read(path_file_config)
    default_config = dict(config_file['default'])
    return default_config


def test_unknown_items(list_items, list_known_items, name_test):

    new_items = []
    for item in list_items:
        if item not in list_known_items and item == item:
            new_items.append(item)
    if len(new_items) != 0:
        if len(new_items) > 1:
            str_items = ', '.join(new_items)
        else:
            str_items = new_items[0]
        logging.info(f"Found {name_test} not known: {str_items}")
        return False
    else:
        return True


def test_file_close(path_file):

    try:
        file_obj = open(path_file, "r+")
        file_obj.closed
        return True
    except IOError:
        logging.error("\nCould not open file! " +
                      f"Please close the file!\n{path_file}\n")
        return False