import configparser
from pyspark import SparkConf


def get_config(env):
    config = configparser.ConfigParser()
    config.read("conf/sbdl.conf")
    conf = {}
    for key, value in config.items(env):
        conf[key] = value

    return conf
