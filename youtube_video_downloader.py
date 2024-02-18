# import streamlit as st
# from pytube import YouTube

# st.title("YouTube Video Downloader")

# video_url = st.text_input("Enter YouTube Video URL", "")
# video_format = st.radio("Select Format", ["mp3", "mp4"])

# if video_url:
#     yt = YouTube(video_url)
#     st.write("Title:", yt.title)
#     st.write("Views:", yt.views)
#     st.write("Duration:", yt.length)
#     st.write("Description:", yt.description)
#     st.write("Ratings:", yt.rating)
#     st.image(yt.thumbnail_url)

#     if st.button("Download"):
#         if video_format == "mp3":
#             audio_stream = yt.streams.filter(only_audio=True).first()
#             audio_stream.download()
#             st.write("Downloaded as MP3")
#         else:
#             video_stream = yt.streams.get_highest_resolution()
#             video_stream.download()
#             st.write("Downloaded as MP4")

# import streamlit as st
# from pytube import YouTube
# import os

# # Setting the title and the description
# st.title("YouTube Video Downloader")
# st.write(
#     """
#     ## Description
#     This application is a simple YouTube Video Downloader. You just need to paste the YouTube video URL 
#     in the input field and then select the desired format (MP3 or MP4). Depending on your selection, 
#     you will be presented with different quality options to download from. Simply select your preferred 
#     quality and click on 'Download' to start the download.
#     """
# )

# video_url = st.text_input("Enter YouTube Video URL", "")

# if video_url:
#     yt = YouTube(video_url)
#     st.write("### Video Details")
#     st.write("Title:", yt.title)
#     st.write("Views:", yt.views)
#     st.write("Duration:", yt.length, "seconds")
#     st.image(yt.thumbnail_url)
#     st.write("")

#     video_format = st.radio("Select your Download Format", ["MP3", "MP4"])

#     if video_format == "MP3":
#         audio_streams = yt.streams.filter(only_audio=True).all()
#         audio_quality = [
#             f"{stream.mime_type} - {stream.abr}" for stream in audio_streams
#         ]
#         selected_audio_quality = st.selectbox("Select Quality", audio_quality)

#         if st.button("Download"):
#             selected_audio_stream = audio_streams[
#                 audio_quality.index(selected_audio_quality)
#             ]
#             file_path = selected_audio_stream.download()
#             new_file_path = os.path.splitext(file_path)[0] + ".mp3"
#             os.rename(file_path, new_file_path)
#             st.write("Downloaded as MP3")

#     else:
#         video_streams = yt.streams.filter(file_extension="mp4").all()
#         video_quality = [f"{stream.resolution}" for stream in video_streams]
#         selected_video_quality = st.selectbox("Select Quality", video_quality)

#         if st.button("Download"):
#             selected_video_stream = video_streams[
#                 video_quality.index(selected_video_quality)
#             ]
#             selected_video_stream.download()
#             st.write("Downloaded as MP4")


import streamlit as st
from pytube import YouTube
import os
from streamlit_lottie import st_lottie
import requests

# Load Lottie URL
# lottie_url = "https://lottie.host/9db09d5a-4049-46db-9bf2-52f16e87ca64/36clxSPZK9.json"
lottie_url = "https://lottie.host/74068b2a-7b7f-4799-aafe-5b43c4c3158d/kMrHvIV5IO.json"
r = requests.get(lottie_url)
if r.status_code != 200:
    st.write("Failed to retrieve Lottie animation.")
else:
    st_lottie(r.json())




# Setting the title and the description
st.title("YouTube Video Downloader :arrow_down:")
st.write(
    """
    ## Description :clipboard:
    This application is a simple YouTube Video Downloader. You just need to paste the YouTube video URL 
    in the input field and then select the desired format (MP3 or MP4). Depending on your selection, 
    you will be presented with different quality options to download from. Simply select your preferred 
    quality and click on 'Download' to start the download.
    """
)

video_url = st.text_input("Enter YouTube Video URL :link:", "")

if video_url:
    yt = YouTube(video_url)
    st.write("### Video Details :film_frames:")
    st.write("Title:", yt.title)
    st.write("Views:", yt.views)
    st.write("Duration:", yt.length, "seconds")
    st.image(yt.thumbnail_url)
    st.write("")

    video_format = st.radio("Select your Download Format :arrow_forward:", ["MP3", "MP4"])

    if video_format == "MP3":
        audio_streams = yt.streams.filter(only_audio=True).all()
        audio_quality = [
            f"{stream.mime_type} - {stream.abr}" for stream in audio_streams
        ]
        selected_audio_quality = st.selectbox("Select Quality :sound:", audio_quality)

        if st.button("Download :arrow_down:"):
            selected_audio_stream = audio_streams[
                audio_quality.index(selected_audio_quality)
            ]
            file_path = selected_audio_stream.download()
            new_file_path = os.path.splitext(file_path)[0] + ".mp3"
            os.rename(file_path, new_file_path)
            st.write("Downloaded as MP3 :white_check_mark:")

    else:
        video_streams = yt.streams.filter(file_extension="mp4").all()
        video_quality = [f"{stream.resolution}" for stream in video_streams]
        selected_video_quality = st.selectbox("Select Quality :high_brightness:", video_quality)

        if st.button("Download :arrow_down:"):
            selected_video_stream = video_streams[
                video_quality.index(selected_video_quality)
            ]
            selected_video_stream.download()
            st.write("Downloaded as MP4 :white_check_mark:")

