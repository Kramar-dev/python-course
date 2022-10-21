import time

from audio_controller import AudioController
import unittest
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.api.audioclient import ISimpleAudioVolume
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class TestAudioController(unittest.TestCase):
	__controller = AudioController()
	
	def test_mute(self):
		self.__controller.mute()
		self.assertTrue(self.__controller.get_volume() <= 0, True)
	
	def test_unmute(self):
		self.__controller.unmute()
		level = self.__controller.get_volume()
		self.__controller.mute()
		self.__controller.unmute()
		self.assertEqual(level, self.__controller.get_volume())
		

	def test_set_volume(self):
		# self.__controller.set_volume(-65.25)
		# i = -65.25
		# counter = 0
		# while counter <= 100:
		# 	level = self.__controller.get_volume()
		#
		# 	print(f"[{counter}][{level}]")
		# 	i+=5
		# 	counter+=1
		# 	self.__controller.set_volume(i)
		# 	time.sleep(0.2)
		self.__controller.set_volume(0.5)
		
"""
-65.25 - 0
-60 - 1
-57 - 1
-55 - 1
-53 - 2
-52 - 2
-50 - 2
-49 - 3
-48 - 3
-47 - 3
-46 - 4
-44 - 4
-43 - 5
-41 - 5
-40 - 6
-39 - 6
-38 - 7
-37 - 8
-36 - 8
-35 - 9
-34 - 9
-33 - 10
-32 - 11
-31 - 12
-30 - 13
-25 - 18
-20 - 26
-15 - 36
-10 - 51
-7 - 63
-5 - 72
-4 - 77
-3.5 - 79
-3 - 82
-2 - 88
-1 - 94
0 - 100
"""