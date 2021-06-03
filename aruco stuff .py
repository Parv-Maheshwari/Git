import glob
import cv2 
import numpy as np
import cv2.aruco as aruco
import math

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:9,0:6].T.reshape(-1,2)

objpoints = []
imgpoints = []

images = glob.glob(r'C:\Users\himad\OneDrive\NokiaXpress\Public\Pictures\Task 5 Data\*.jpg')
idx = 0
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret,corners = cv2.findChessboardCorners(gray,(9,6),None)
    
    print(ret)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray, corners, (11,11),(-1,-1), criteria)
        imgpoints.append(corners)

        cv2.drawChessboardCorners(img,(9,6), corners2, ret)
        cv2.imwrite("img_chess%d.jpg"%idx, img)

    idx += 1
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

inputImage = cv2.imread(r'C:\Users\himad\Downloads\aruco.jpg')
arucoDict = aruco.Dictionary_get(aruco.DICT_5X5_250)
arucoParams = aruco.DetectorParameters_create()
(corners,ids,rejected) = aruco.detectMarkers(inputImage,arucoDict,parameters = arucoParams)
aruco.drawDetectedMarkers(inputImage,corners,ids)
cv2.imwrite("aruco.jpg", inputImage)
rvec,tvec,markerPoints = aruco.estimatePoseSingleMarkers(corners,97,mtx,dist)
aruco.drawAxis(inputImage,mtx,dist,rvec,tvec,50)
cv2.imwrite("pose_estimate.jpg",inputImage)
rmat,jacobian = cv2.Rodrigues(rvec)
print(rmat)
tvec =np.array(tvec.tolist()[0][0])
x,y,z = np.matmul(-np.transpose(rmat),tvec)
print(x)
print(y)
print(z)

#yaw is alpha 
#pitch is beta 
#roll is gamma 

alpha = math.atan(rmat[1,0]/rmat[0,0])
beta = math.atan(-rmat[2,0]/math.sqrt((rmat[2,1])**2 + (rmat[2,2])**2))
gamma = math.atan(rmat[2,1]/rmat[2,2])

print(alpha)
print(beta)
print(gamma)
