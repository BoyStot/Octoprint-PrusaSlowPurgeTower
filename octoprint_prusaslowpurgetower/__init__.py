# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import octoprint.filemanager
import octoprint.filemanager.util

psw_std_feedrates = ''
psw_slow_feedrate = ['60']

class PrusaSlowPurgeTower(octoprint.filemanager.util.LineProcessorStream):
	def process_line(self, line):
		global psw_std_feedrates, psw_slow_feedrate
		
		__line = line
		
		if('PURGESPEED' in line):
			# Keep gcode set feedrates for returning to after slow down.
			psw_slow_feedrate = [int(s) for s in __line.replace(':',' ').split() if s.isdigit()]
			#psw_slow_feedrate = str(__line.split(':'))
		elif('M203' in line):
			# Keep gcode set feedrates for returning to after slow down.
			psw_std_feedrates = line
		elif('; CP TOOLCHANGE WIPE' in line):
			# Insert code to slow down the purge tower.
			__line = __line + "M203 X" + str(psw_slow_feedrate[0]) + " Y" + str(psw_slow_feedrate[0]) + " Z6 E60 ; slow down tower wipe.\n"
		elif('; CP TOOLCHANGE END' in line):
			# Insert code to restore speed.
			__line = __line + psw_std_feedrates + "; Back to normal.\n"
		return __line

def add_feed_limits(path, file_object, links=None, printer_profile=None, allow_overwrite=True, *args, **kwargs):
	if not octoprint.filemanager.valid_file_type(path, type="gcode"):
		return file_object

	import os

	return octoprint.filemanager.util.StreamWrapper(file_object.filename, PrusaSlowPurgeTower(file_object.stream()))

__plugin_name__ = "Prusa Slow Purge Tower"
__plugin_description__ = "Slows down the wipe on the colour change tower to help with toothpaste stripe smearing and bridging issues."
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_hooks__ = {
    "octoprint.filemanager.preprocessor": add_feed_limits
}
