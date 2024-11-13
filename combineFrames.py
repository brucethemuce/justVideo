import cv2
import numpy as np
fps=240
xres=1000
yres=2000

def concatenate_videos(new_video_path, videos):
    output = cv2.VideoWriter(new_video_path, cv2.VideoWriter_fourcc(*"MPEG"), fps, frameSize=(xres,yres))
    while True:
        r1, frame1 = videos[0].read()
        r2, frame2 = videos[1].read()
        r3, frame3 = videos[2].read()
        r4, frame4 = videos[3].read()
        if not r1 or not r2 or not r3 or not r4: #break when any video runs out of frames, make robuster
            break
        canvas=np.zeros((xres,yres*4,3),dtype=np.uint16) #p. should be 10bit
        
        #place each read frame onto the canvas in their positions
        canvas[0:yres, :]           = frame1 
        canvas[yres+1:yres*2, :]    = frame2
        canvas[2*yres+1:yres*3, :]  = frame3
        canvas[3*yres+1:, :]        = frame4
        #assumes no overlap of pixels, fix later
        output.write(canvas)
        
    #release all files
    videos[0].release()
    videos[1].release()
    videos[2].release()
    videos[3].release()
    output.release()
    
videoList = ["A.mp4", "B.mp4", "C.mp4", "D.mp4"]
concatenate_videos("combined.mp4",videoList)