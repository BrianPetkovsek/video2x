#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: FFMPEG Class
Author: K4YT3X
Date Created: Feb 24, 2018
Last Modified: May 19, 2018

Description: This class controls waifu2x
engine

Version 2.0.1
"""
import subprocess


class WAIFU2X:
    """This class communicates with waifu2x cui engine

    An object will be created for this class, containing information
    about the binary address and the processing method. When being called
    by the main program, other detailed information will be passed to
    the upscale function.
    """

    def __init__(self, waifu2x_path, method, model_type):
        self.waifu2x_path = waifu2x_path
        self.method = method
        self.model_type = model_type

    def upscale(self, folderin, folderout, width, height):
            """This is the core function for WAIFU2X class

            Arguments:
                folderin {string} -- source folder path
                folderout {string} -- output folder path
                width {int} -- output video width
                height {int} -- output video height
            """
            execute = "{} -p {} -I png -i {} -e png -o {} -w {} -h {} -n 3 -m noise_scale -y {}".format(
                self.waifu2x_path, self.method, folderin, folderout, width, height, self.model_type)
            subprocess.call(execute)