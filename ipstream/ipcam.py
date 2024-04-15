import subprocess

# Replace these with your desired settings
webcam_device = 'HD User Facing'  # Adjust if your webcam has a different device number
rtsp_port = 8554  # You can change this port if needed
stream_path = "mystream"  # Customize the path in the RTSP URL

# Build the ffmpeg command for RTSP streaming
ffmpeg_cmd = [
    "ffmpeg",
    "-f", "dshow",  # Use dshow for Windows
    "-i", f"video={webcam_device}",  # Device name for dshow
    "-pix_fmt", "yuv420p",
    "-c:v", "libx264",
    "-preset", "ultrafast",  # Adjust encoding speed (faster preset)
    "-b:v", "9600k",  # Lower bitrate
    "-rtbufsize", "1024M",  # Increase buffer size
    "-f", "rtsp",
    f"rtsp://localhost:{rtsp_port}/{stream_path}"
]

# Start the streaming process using subprocess
process = subprocess.Popen(ffmpeg_cmd)

# Keep the script running while ffmpeg streams
try:
    while True:
        process.wait()  # Wait for ffmpeg to finish (should never reach here)
except KeyboardInterrupt:
    # Exit script on keyboard interrupt (Ctrl+C)
    process.terminate()
    print("Streaming stopped!")
