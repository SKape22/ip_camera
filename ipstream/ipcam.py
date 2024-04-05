import cv2
from flask import Flask, Response

# Initialize Flask application
app = Flask(__name__)

def generate_frames():
    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    # Set codec and video parameters
    codec = cv2.VideoWriter_fourcc(*'XVID')
    fps = 20
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create VideoWriter object for RTSP streaming
    out = cv2.VideoWriter("rtsp://127.0.0.1:8554/test", codec, fps, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to receive frame.")
            break

        # Write frame to VideoWriter object
        out.write(frame)

        # Encode the frame in JPEG format
        ret, buffer = cv2.imencode('.jpg', frame)

        if not ret:
            print("Error: Failed to encode frame.")
            break

        # Convert the frame to bytes
        frame_bytes = buffer.tobytes()

        # Yield the frame in bytes
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    # Release resources
    cap.release()
    out.release()

@app.route('/')
def index():
    # Return the streaming response
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
