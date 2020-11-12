import pytube
"""
    Download Youtube video using iTag from pytube module.
    File are saved in downloadPath
"""

url = input("Enter the youtube URL ")
downloadPath = r"/Users/user/Downloads"
iTag = ""

try:
    youtube = pytube.YouTube(url)
    print(f'The youtube title is "{youtube.title}"')
    streams = youtube.streams
    for i in streams:
        try:
            print(i)
        except:
            print("video not available")
            iTag = None
    if iTag != None:
        try:
            iTag = int(input("Enter the iTag number "))
            print(f'Downloading video {youtube.title} with iTag {iTag}')
            video = youtube.streams.get_by_itag(iTag)
            video.download(downloadPath)
            print(f'Downloaded file to path {downloadPath}')
        except:
            print('iTag not available')
except:
    print('URL provided is not recogonized. Exiting program')
