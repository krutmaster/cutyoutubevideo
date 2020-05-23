from pytube import YouTube
import subprocess

raw = input().split()
link = raw[0]
quality = int(raw[1])
fps = int(raw[2])
ss = raw[3]
t = raw[4]

if quality == 720:
    itag = 22
    url = YouTube(link).streams.get_by_itag(itag).url

    if fps <= 30:
        bit_v = 5000
    else:
        bit_v = 7500

    file_name = 'output720.mp4'
    process_call_str = f'ffmpeg -ss {ss} -to {t} -i "{url}" -b:a 320k -b:v {bit_v}k -r {fps} -avoid_negative_ts make_zero "{file_name}"'
else:
    aurl = YouTube(link).streams.get_by_itag(18).url

    if quality == 1080:
        itag = 137
        url = YouTube(link).streams.get_by_itag(itag).url
        if fps <= 30:
            bit_v = 8000
        else:
            bit_v = 12000

        file_name = 'output1080.mp4'

    '''
    elif quality == 480:
        itag = don't know itag for 480p. Will add later
        url = YouTube(link).streams.get_by_itag(itag).url
        file_name = 'output480.mp4'
    '''

    process_call_str = f'ffmpeg -ss {ss} -to {t} -i "{url}" -ss {ss} -to {t} -i "{aurl}" -b:a 320k -b:v {bit_v}k -r {fps} -avoid_negative_ts make_zero -map 0:v:0 -map 1:a:0 "{file_name}"'

status = subprocess.check_call(process_call_str, shell=True)
