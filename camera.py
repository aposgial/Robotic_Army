import cv2


class Camera():
    def __init__(self) -> None:
        pass
    
    def open_camera(self):
        # Open the default camera
        cap = cv2.VideoCapture(0)

        # Check if the camera is opened successfully
        if not cap.isOpened():
            print("Failed to open the camera.")
            return

        # Read and display frames from the camera
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # If the frame was not captured successfully, exit the loop
            if not ret:
                break

            # Display the resulting frame
            cv2.imshow('Camera', frame)

            # Wait for 'q' key to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    cam = Camera()
    cam.open_camera()