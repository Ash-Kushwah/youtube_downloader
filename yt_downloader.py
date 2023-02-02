from pytube import YouTube

# Getting the link from the user
link = input("Give the link of the video you want downlaod: ")
yt = YouTube(link)

# Printing the video title and views
print("Title: ", yt.title)
print("Views: ", yt.views)

# Asking for resolution to download 
print("In which resolution you want to download ?\n" "Available Options: 720p, 360p")
res = input("Paste here: ")

def downloadVdo(res):
    print("Sending request...")
    yd = yt.streams.get_by_resolution(res)
    print("Response received. \nPreparing to Download !")
    # Initializing the folder in which we want to download 
    yd.download("E:\Downloads\yt Downloads")
    print("download complete")

downloadVdo(res)
