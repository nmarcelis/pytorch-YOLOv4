from demo import detect_cv2, detect_cv2_camera


cfgfile = "/home/niels/workspaces/detection-networks-ws/pytorch-yolov4-ws/src/pytorch-YOLOv4/cfg/yolov4-tiny.cfg"
weightfile = "/home/niels/workspaces/detection-networks-ws/pytorch-yolov4-ws/src/pytorch-YOLOv4/weights/yolov4-tiny.weights"
imgfile = "/home/niels/workspaces/detection-networks-ws/pytorch-yolov4-ws/src/pytorch-YOLOv4/data/dog.jpg"

pthfile = "/home/niels/workspaces/detection-networks-ws/pytorch-yolov4-ws/src/pytorch-YOLOv4/weights/yolov4.pth"

if __name__ == '__main__':
    detect_cv2(cfgfile, weightfile, imgfile)


    # detect_cv2_camera(cfgfile, weightfile)
