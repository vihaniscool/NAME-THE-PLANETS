import cv2

img = cv2.imread("solar-system.jpg") 
cv2.putText(img,
            "Sun",
            (100,90),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,225)
            )

cv2.putText(img,
            "Mercury",
            (110,187),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Vence",
            (190,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Earth",
            (288,265),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Mars",
            (380,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )

cv2.putText(img,
            "Jupiter",
            (550,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )

cv2.putText(img,
            "Saturn",
            (750,120),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )

cv2.putText(img,
            "Uranus",
            (930,140),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )

cv2.putText(img,
            "Neptune",
            (1070,147),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )

cv2.imshow("output",img)
cv2.waitKey(0)