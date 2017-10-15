# -*- coding: utf-8 -*-
"""
环境配置文件
"""



class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True