import os
import configparser

cfg_file = "joe.conf"

config = configparser.ConfigParser()
config.read(cfg_file)

cfg = config

def reread_config():
    config = configparser.ConfigParser()
    config.read(cfg_file)

    cfg = config


def write_config(key, value):

    cfg[key] = value

    with open(cfg_file, w) as configfile:
        config.write(cfg)
    configfile.close()


def write_complete_config(config):
    with open(cfg_file, w) as configfile:
        config.write(config)
    configfile.close()

    cfg = config
