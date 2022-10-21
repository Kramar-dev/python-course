from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.api.audioclient import ISimpleAudioVolume
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class AudioController:
	def __init__(self):
		devices = AudioUtilities.GetSpeakers()
		interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
		self.__volume = cast(interface, POINTER(IAudioEndpointVolume))
		
		sessions = AudioUtilities.GetAllSessions()
		for session in sessions:
			volume = session._ctl.QueryInterface(ISimpleAudioVolume)
			if session.Process and session.Process.name() == "vlc.exe":
				print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
				volume.SetMasterVolume(0.6, None)
	
	
	
	def mute(self):
		self.__volume.SetMute(1, None)
	
	def unmute(self):
		self.__volume.SetMute(0, None)
	
	def get_volume(self):
		return self.__volume.GetMasterVolumeLevel()
	
	"""
	1 - x
	-65.25 - 100

	"""
	def set_volume(self, level: float):
		self.__volume.SetMasterVolumeLevelScalar(level, None)
