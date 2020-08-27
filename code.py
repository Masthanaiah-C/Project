import cv2
j=cv2.imread("/Users/DELL/Desktop/Project/ab.png")
cv2.imshow("sucess",j)
cv2.imwrite("/Users/DELL/Desktop/image.png",j)
cv2.waitKey(0)
cv2.destroyAllWindows()
