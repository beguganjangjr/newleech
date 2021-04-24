#!/usr/bin/env python3
# -*- coding: utf-8 -*-
<<<<<<< HEAD
# (c) @TN57_BotZ
=======
# (c) Shrimadhav U K
>>>>>>> c863725f40d16c2ad68e86602bc4a6e1c38c58b8

import logging
import os
import time
from shutil import copyfile


async def copy_file(input_file, output_dir):
    output_file = os.path.join(output_dir, str(time.time()) + ".jpg")
    # https://stackoverflow.com/a/123212/4723940
    copyfile(input_file, output_file)
    return output_file
