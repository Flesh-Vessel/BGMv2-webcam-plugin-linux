import cv2
import pyvirtualcam


device_id = 1  # try 0, 1, 2 ...

cap = cv2.VideoCapture(device_id)
print("cap isOpened", cap.isOpened())

ret, frame = cap.read()
print("get frame", ret)

try:
    while True:
        with pyvirtualcam.Camera(
            height=480,
            width=640,
            fps=15,
            print_fps=True,
            fmt=pyvirtualcam.PixelFormat.BGR,
            device="Unity Video Capture",
            backend="unitycapture",
        ) as cam:
            ret, frame = cap.read()
            cv2.imshow("frame", frame)
            cv2.waitKey(1)
            cam.send(frame)
            cam.sleep_until_next_frame()

except KeyboardInterrupt:
    cv2.destroyAllWindows()
    cap.release()
