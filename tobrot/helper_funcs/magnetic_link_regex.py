#!/usr/bin/env python3
# -*- coding: utf-8 -*-
<<<<<<< HEAD
# (c) @TN57_BotZ
=======
# (c) Shrimadhav U K
>>>>>>> c863725f40d16c2ad68e86602bc4a6e1c38c58b8

import logging
import os
import re


MAGNETIC_LINK_REGEX = r"magnet\:\?xt\=urn\:btih\:([A-F\d]+)"


def extract_info_hash_from_ml(magnetic_link):
    ml_re_match = re.search(MAGNETIC_LINK_REGEX, magnetic_link)
    if ml_re_match is not None:
        return ml_re_match.group(1)
