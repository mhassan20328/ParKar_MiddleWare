from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
import os

def extract_frames(video_path, output_folder, interval_sec=5):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load the video clip
    clip = VideoFileClip(video_path)

    # Get the duration of the video
    total_duration = clip.duration

    print(f"Video Duration: {total_duration} seconds")

    frame_num = 0
    current_time = 0

    while current_time < total_duration:
        # Get the frame at the current time
        frame = clip.get_frame(current_time)

        # Create an ImageClip from the frame
        img_clip = ImageClip(frame)

        # Save the image
        image_filename = os.path.join(output_folder, f"frame_{frame_num}.jpg")
        img_clip.save_frame(image_filename)

        print(f"Frame {frame_num + 1} saved: {image_filename}")

        # Increment frame number
        frame_num += 1

        # Update current time for the next iteration
        current_time += interval_sec

    print("Frames extraction completed.")

if __name__ == "__main__":
    # Specify the path to the video file
    video_path = "C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/Screenshot middleware/testvid.mp4"

    # Specify the output folder for the JPEG images
    output_folder = "C:/Users/mazen/OneDrive/Documents/AUC/Thesis/Middleware/Screenshot middleware/screenshots"

    # Specify the interval between frames in seconds (e.g., 5 seconds)
    capture_interval = 5

    extract_frames(video_path, output_folder, interval_sec=capture_interval)
