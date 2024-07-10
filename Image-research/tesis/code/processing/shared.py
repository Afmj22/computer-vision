import matplotlib.pyplot as plt

def display_imgs(imgs = [], titles = []):
    plt.figure(figsize=(5, 5))
    for i in range(len(imgs)):
        plt.subplot(1, len(imgs), i+1)
        plt.imshow(imgs[i])
        plt.title(titles[i])
        plt.axis('off')
    plt.tight_layout()
    plt.show()

def display_plots(plots = [], titles = []):
    plt.figure(figsize=(4, 4))
    for i in range(len(plots)):
        plt.subplot(1, len(plots), i+1)
        plt.plot(plots[i])
        plt.title(titles[i])
    plt.tight_layout()
    plt.show()