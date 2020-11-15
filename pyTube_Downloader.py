import pytube
"""
    Download Youtube video using iTag from pytube module.
    File are saved in downloadPath
"""

url = input("\nEnter the youtube URL ")
downloadPath = r"/Users/user/Downloads"
audio = "mp4a.40.2"
iTag = ""

try:
    youtube = pytube.YouTube(url)
    print(f'\nThe youtube title is "{youtube.title}"\n')
    streams = youtube.streams
    audioVideo = input("Enter 'V' for video 'A' for audio ")
    if len(audioVideo) == 0 or audioVideo.upper() == 'V':
        i = "video/mp4"
    else:
        i = "audio/mp4"
    print(f'\nThe available streams for {i}\n')
    for entry in streams:
        if i in str(entry) and audio in str(entry):
            try:
                print(entry)
            except:
                print("video not available")
                iTag = None
    if iTag != None:
        try:
            iTag = int(input("\nEnter the iTag number "))
            print(f'\nDownloading video {youtube.title} with iTag {iTag}')
            video = youtube.streams.get_by_itag(iTag)
            video.download(downloadPath)
            print(f'\nDownloaded file to path {downloadPath}')
        except:
            print('\niTag not available')
except:
    print('URL provided is not recogonized. Exiting program')
