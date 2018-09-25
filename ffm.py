import ffmpeg
infile = ffmpeg.input('input.mp4')
outfile = ffmpeg.output(infile, 'output.mp3')
ffmpeg.run(outfile)

from ffmpeg import video
input_file = "input.mp4"
out_file = "output.mp4"
video.separate_audio(input_file, out_file)