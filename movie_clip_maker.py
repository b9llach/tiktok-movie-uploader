from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import mirror_x
import math
from tiktok_uploader.upload import upload_video
import argparse

def split_video(input_file, output_name, clip_duration, headless):
    video = VideoFileClip(input_file)
    total_duration = video.duration
    num_clips = math.ceil(total_duration / clip_duration)

    for i in range(num_clips):
        start_time = i * clip_duration
        end_time = min((i + 1) * clip_duration, total_duration)
        clip = video.subclip(start_time, end_time)
        flipped_clip = clip.fx(mirror_x)

        output_path = f"./clips/{output_name}_{i+1}.mp4"
        flipped_clip.write_videofile(output_path)
        upload_video(output_path, '#fyp', cookies='cookies.txt',headless=headless)

    video.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputfile', type=str, help='Name of input file')
    parser.add_argument('--outputfile', type=str, help='Name of output file')
    parser.add_argument('--duration', type=int, help='Length of clip')
    parser.add_argument('--headless', type=bool, help='Headless browser so it doesn\'t show up on screen',default=True)

    args = parser.parse_args()
    split_video(input_file=args.inputfile,output_name=args.outputfile,clip_duration=args.duration,headless=args.headless)

if __name__ == "__main__":
    main()


