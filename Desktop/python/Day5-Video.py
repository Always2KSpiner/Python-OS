import cv2 as cam # import computer Vision Module
capt=cam.VideoCapture(0) #start video capture
#print(stat) #print Status
while True: #inifnte loop
    stat,pic=capt.read() # save status and picture in variables
    cam.imshow("Press Enter to Exit",pic) # show pic in a Window called Test1
    if cam.waitKey(1)==13:#Hold the window on screen and Refresh it every 1ms (move forward when a 'Enter' is detected)
        break #Break Infinite Loop
cam.destroyAllWindows() #Close the window
capt.release() #Release Camera Resource
