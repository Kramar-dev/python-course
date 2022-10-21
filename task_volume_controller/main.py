from audio_controller import AudioController


def main():
    controller = AudioController()
    controller.mute()
    controller.unmute()


if __name__ == "__main__":
    main()
