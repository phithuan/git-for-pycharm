import sys
import ffmpeg

sys.path.append(r'D:\FFmepg\ffmpeg-2023-02-22-git-d5cc7acff1-essentials_build\bin') #đường dẫn ffmpeg



stream = ffmpeg.input("Tin • Instagram - Google Chrome 2023-01-02 19-43-03.mp4")
stream = stream.trim(start=0,duration=5).filter("setpts","PTS-STARTPTS")
stream = ffmpeg.output(stream,"output.mp4")
ffmpeg.run(stream)