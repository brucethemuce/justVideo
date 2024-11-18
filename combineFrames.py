import cv2
import numpy as np
fps=240
xres=1520
yres=2704

def concatenate_videos(new_video_path, videos):
    output = cv2.VideoWriter(new_video_path, cv2.VideoWriter_fourcc(*"MPEG"), fps, frameSize=(xres,yres))
    i=1
    while i<60:
        print(i)
        r1, frame1 = cv2.VideoCapture(videos[0]).read()
        r2, frame2 = cv2.VideoCapture(videos[1]).read()
        r3, frame3 = cv2.VideoCapture(videos[2]).read()
        if not r1 or not r2 or not r3: #break when any video runs out of frames, make robuster
            break
        
        #place each read frame onto the canvas in their positions
        canvas = np.concatenate((frame1,frame2,frame3),axis=0)
        
        #assumes no overlap of pixels, fix later
        output.write(canvas)
        i=i+1
        
    #release all files
    cv2.VideoCapture(videos[0]).release()
    cv2.VideoCapture(videos[1]).release()
    cv2.VideoCapture(videos[2]).release()

    output.release()
    
videoList = ["A.mp4", "B.mp4", "C.mp4"]
concatenate_videos("combined.mp4",videoList)