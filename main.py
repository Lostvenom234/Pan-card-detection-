from skimage.metrics import structural_similarity as ssim
import imutils
import cv2
from PIL import Image
import requests
!mkdir pancard_tamperings
!mkdir pancard_tamperings/images
original = original_image.resize((250, 160))
original.save('pancard_tamperings/images/original.png')
tampered = tampered_image.resize((250, 160))
tampered.save('pancard_tamperings/images/tampered.png')
print(original)
print(tampered)
original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
tampered_gray = cv2.cvtColor(tampered_image, cv2.COLOR_BGRA2GRAY)
(score, diff) = ssim(original_gray, tampered_gray, full=True)
diff = (diff * 255).astype("uint8")
diff= diff * 255
diff = diff.astype("uint8")
threshold=  cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)  
for c in cnts:
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(tampered_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
Image.fromarray(original_image)
Image.fromarray(tampered_image)
Image.fromarray(diff)
Image.fromarray(threshold)
