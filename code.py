import cv2
new_y=int(input("y in in pixels:"))
new_x=int(input(" x in pixels:"))
b=cv2.imread("/Users/DELL/Desktop/Project/ab.png")
m=b.shape

y=m[0]//new_y
x=m[1]//new_x
for i in range(x):
    for j in range(y):
        k=b[new_y*j:new_y*(j+1), new_x*i:new_x*(i+1)]
        cv2.imwrite("/Users/DELL/Desktop/Project/crop/"+str(j)+"-"+str(i)+".png",k)
        

cv2.destroyAllWindows()
