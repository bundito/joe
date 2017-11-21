import os
import configparser

cfg_file = "joe.conf"

config = configparser.ConfigParser()
config.read(cfg_file)

cfg = config

print("XXX")
print(cfg)
print("XXX")

def reread_config():
    cfg_file = "joe.conf"

    config = configparser.ConfigParser()
    config.read(cfg_file)

    return config

def write_config(key, value):

    cfg_file = "joe.conf"
    cfg[key] = value

    with open(cfg_file, 'w') as configfile:
        configfile.write(cfg)
    configfile.close()


def write_complete_config(configdata):

    cfg_file = "joe.conf"

    with open(cfg_file, 'w') as configfile:
        configdata.write(configfile)


