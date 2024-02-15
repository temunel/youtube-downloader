import pytube

def download(youtube_video_link):
    try:
        print("Downloading...")
        youtubelink=pytube.YouTube(youtube_video_link)
        video=youtubelink.streams.get_highest_resolution()        
        video.download()
        print("Video Downloaded!")
    except:
        print("Invalid Link!")

if __name__ == "__main__":
    youtube_video_link = input("Input Youtube Video Link: ")
    download(youtube_video_link)