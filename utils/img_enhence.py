import cv2
import numpy as np


def adjust_gamma(image, gamma=1.0):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")


    return cv2.LUT(image, table)


def enhance_image(image):

    img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    image = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(blurred, -1, filter)


    gamma_adjusted = adjust_gamma(sharpened, gamma=1.2)

    return gamma_adjusted


def denoise_and_enhance(input_path, output_path):

    image = cv2.imread(input_path)

    if image is None:
        raise ValueError("Image not loaded correctly. Please check the file path.")


    enhanced_image = enhance_image(image)

    denoised_image = cv2.fastNlMeansDenoisingColored(enhanced_image, None, 10, 10, 7, 21)

    cv2.imwrite(output_path, denoised_image)
    print(f"Denoised and enhanced image saved to {output_path}")

