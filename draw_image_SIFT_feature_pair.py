import cv2
import cv2.xfeatures2d as cv
import numpy
from matplotlib import pyplot as plt


def SIFT_feature_matching(img1, img2, n=1000):
    t1 = cv2.imread(img1,-1)
    t2 = cv2.imread(img2,-1)

    sift=cv.SIFT_create()

    kp1, des1 = sift.detectAndCompute(t1, None)
    kp2, des2 = sift.detectAndCompute(t2, None)

    f=cv2.drawKeypoints(t1,kp1,None,[0,0,255],flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    nf=cv2.drawKeypoints(t2,kp2,None,[255,0,0],flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    bf = cv2.BFMatcher()
    matches=bf.match(des1,des2)

    matches = sorted(matches, key = lambda x:x.distance)

    result=cv2.drawMatches(t1,kp1,t2,kp2,matches[:min(n,len(matches))],None,[0,0,255],flags=2)

    cv2.imwrite("result.png", result)
    cv2.imshow("ss", result)
    cv2.waitKey(0)
    # plt.imshow(result, interpolation = 'bicubic')
    # plt.axis('off')
    # plt.show()


if __name__ == "__main__":
    SIFT_feature_matching("morning.png", "afternoon.png", n=100)
