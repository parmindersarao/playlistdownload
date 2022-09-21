import os
import re
import argparse
import sys
import moviepy.editor as mp
from pytube import YouTube
from pytube import Playlist

def playlistDownload(url,OA,d):
    link=url
    folder=d
    playlist = Playlist(link)
    for url in playlist:
        print(url)
    for vid in playlist.videos:
        print(vid)

    for url in playlist:
        YouTube(url).streams.filter(file_extension="mp4").first().download(folder)
        if(OA=='t'):
            for file in os.listdir(folder):
                if re.search('mp4', file):
                    mp4_path = os.path.join(folder,file)
                    mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
                    new_file = mp.AudioFileClip(mp4_path)
                    new_file.write_audiofile(mp3_path)
                    os.remove(mp4_path)


def ytvDownload(url,OA,d):
    YouTube(url).streams.filter(file_extension="mp4").first().download(d)
    if(OA=='t'):
        for file in os.listdir(d):
                if re.search('mp4', file):
                    mp4_path = os.path.join(d,file)
                    mp3_path = os.path.join(d,os.path.splitext(file)[0]+'.mp3')
                    new_file = mp.AudioFileClip(mp4_path)
                    new_file.write_audiofile(mp3_path)
                    os.remove(mp4_path)


if __name__=="__main__":
    arg=argparse.ArgumentParser()
    arg.add_argument('-p','--playlist',help='if you want to download whole playlist then type t else f',type=str, required=True)
    arg.add_argument('-u','--url',help='url of playlist or single video ',type=str,required=True)
    arg.add_argument('-OA','--onlyaudio',help='if you want to download only audio then type t else f',type=str,required=True)
    arg.add_argument('-d','--dir',help='Direcotary where you want to download',type=str,required=True)

    args=arg.parse_args()

    playlist=args.playlist
    url=args.url
    OA=args.onlyaudio
    d=args.dir

    if((playlist=='t' or playlist=='f')and(OA=='t' or OA=='f')):
        if(playlist=='t'):
            playlistDownload(url,OA,d)
        else:
            ytvDownload(url,OA,d)
    else:
        print('Invalid argument')
        sys.exit()
    