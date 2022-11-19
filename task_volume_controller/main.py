from audio_controller import AudioController


def main():
    controller = AudioController()
    # controller.mute()
    # controller.unmute()
    controller.set_volume(0.10)


if __name__ == "__main__":
    main()
