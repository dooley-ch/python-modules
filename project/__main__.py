import src
import lib


def main():
    greeter = src.GreetTheWorld('Main')
    greeter.say_hello()

    external = lib.ExternalGreeter('External')
    external.say_hello()


if __name__ == '__main__':
    main()
