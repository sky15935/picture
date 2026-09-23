import cv2
import matplotlib.pyplot as plt

def flip_image(image_path):
    """
    输入：图片路径
    输出：在屏幕上显示原始图片和左右翻转后的图片
    """
    img = cv2.imread(image_path)
    if img is None:
        print(f"错误：无法读取图片，请检查路径：{image_path}")
        return

    flipped_img = cv2.flip(img, 1)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    flipped_rgb = cv2.cvtColor(flipped_img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(img_rgb)
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Flipped Image (Left-Right)")
    plt.imshow(flipped_rgb)
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    flip_image("test.jpg")
