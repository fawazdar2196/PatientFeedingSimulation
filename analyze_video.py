import cv2

# Function to analyze the video and print the coordinates of tracked objects
def analyze_video(video_path):
    # Load the video
    cap = cv2.VideoCapture(video_path)

    # Check if video is opened successfully
    if not cap.isOpened():
        print("Error: Cannot open video.")
        return

    # Define the range of the object's color in HSV (adjust according to the object)
    lower_color = (30, 150, 50)  # Lower bound of color (adjust as necessary)
    upper_color = (255, 255, 180)  # Upper bound of color (adjust as necessary)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for the object color
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)

        # Find contours (objects) in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Get the bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the coordinates of the tracked object
            print(f"Coordinates: X: {x}, Y: {y}, Width: {w}, Height: {h}")

        # Show the frame with object tracking
        cv2.imshow('Tracked Object', frame)

        # Press 'q' to exit the video window
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Provide the path to your video file here
video_path = 'New.mp4'
analyze_video(video_path)
