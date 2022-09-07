# -*- coding: utf-8 -*-

import os


class DefaultConfig:
    """Preprocess Configuration"""

    NLP_SECRET = os.environ.get("NLP_SECRET", "xxx")
