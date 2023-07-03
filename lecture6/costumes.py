import sys

from PIL import Image


def main():
    image1()


def image1():
    images = []
    # everything except the 1st element of argv
    for arg in sys.argv[1:]:
        image = Image.open(arg)
        images.append(image)

    images[0].save(
        "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
    )


if __name__ == "__main__":
    main()
