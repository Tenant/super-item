import cv2

def process(inputvideoname):
    # read video, and convert to images
    cap = cv2.VideoCapture(inputvideoname)
    os.makedirs("Camera", exist_ok=True)
    frame_cnt = 0
    while cap.isOpened():
        ret, frame = cap.read()
        frame_cnt += 1
        if ret == 0:
            break
        cv2.imwrite(os.path.join(".", "Camera", str(frane_cnt) + ".png"), frame)
        cv2.imshow('ss', frame)
        cv2.waitKey(100)
    cap.release()
    
if __name__ == '__main__':
    process("l.avi")
