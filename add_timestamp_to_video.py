# -*- coding: utf-8 -*-
import sys
import cv2


def help():
    print("Depencies: python_opencv")
    print("Usage:")
    print("python3 add_timestamp_to_video raw_video.avi timestamp.log processed_video.avi")
    print("python3 add_timestamp_to_video raw_video.avi timestamp.log processed_video.avi true")


def process(inputvideoname, timestampfilename, outputvideoname, verbose=False):
    cap = cv2.VideoCapture(inputvideoname)
    frame_rate = int(round(cap.get(cv2.CAP_PROP_FPS)))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("frame rate: {}, width: {}, height: {}, total frames: {}".format(frame_rate, frame_width, frame_height, frame_number))

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(outputvideoname, fourcc, frame_rate, (frame_width, frame_height))

    timestamp_file = open(timestampfilename, 'r')
    lines = timestamp_file.readlines()
    print("total time records: {}".format(len(lines)))

    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == 0:
            break
        try:
            timestamp = int(lines[i].strip())
        except ValueError:
            print(i)
            print(lines[i])
            continue
                
        cv2.putText(frame, str(timestamp), (50,50), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255))   
        out.write(frame)

        if i % 100 == 0:
            print("process {}/{}".format(i, frame_number))
        i += 1

        if verbose:
            cv2.imshow('ss', frame)
            cv2.waitKey(10)

    cap.release()
    out.release()
    timestamp_file.close()

if __name__ == '__main__':
    if len(sys.argv) == 5:
        process(sys.argv[1], sys.argv[2], sys.argv[3], verbose=True)
    elif len(sys.argv) == 4:
        process(sys.argv[1], sys.argv[2], sys.argv[3], verbose=False)
    else:
        help()
