# -*- coding: utf-8 -*-

import os


class DefaultConfig:
    """ Preprocess Configuration """
    SCRAPPER_SECRET = os.environ.get('SCRAPPER_SECRET', 'xxx')
