import cv2
from matplotlib import pyplot as plt
import os  


def mozaika(images):
    fig, axes = plt.subplots(2, 3, figsize=(10, 6))
    i = 0
    for ax in axes.flat:
        ax.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
        ax.axis('off')
        i += 1

    plt.tight_layout()
    plt.show()




def main():
    planes = ["samolot06.jpg", "samolot08.jpg", "samolot09.jpg", "samolot10.jpg", "samolot12.jpg", "samolot17.jpg"]
    images = []
    
    for plane in planes:
        path = os.path.join("Samoloty", "planes", plane)
        image = cv2.imread(path)
        images.append(image)

    mozaika(images)

main()  