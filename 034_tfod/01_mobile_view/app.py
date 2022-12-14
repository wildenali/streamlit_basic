import cv2
import streamlit as st
import numpy as np
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer
from streamlit_webrtc import WebRtcMode, RTCConfiguration
import av
import base64
from io import BytesIO
from PIL import Image

# Streaming camera using VideoTransformerBase
class VideoTransformer(VideoTransformerBase):
    def __init__(self):
        self.i = 0
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return img

# Streaming camera using frameWindow
def frameWindow(cam, FRAME_WINDOW):
    while True:
        ret, frame = cam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)

# Streaming camera using WebRtcMode, RTCConfiguration
RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)
class VideoProcessor:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        return av.VideoFrame.from_ndarray(img, format="bgr24")



def get_image_download_link(img,filename,text):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href =  f'<a href="data:file/jpg;base64,{img_str}" download="{filename}">{text}</a>'
    return href

def face_detect(image,sf,mn):
    i = 0
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # faces = faceCascade.detectMultiScale(gray,sf,mn)
    # for (x, y, w, h) in faces:
    #     i = i+1
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (237, 30, 72), 3)
    #     cv2.rectangle(image, (x, y - 40), (x + w, y),(237, 30, 72) , -1)
    #     cv2.putText(image, 'F-'+str(i), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    resi_image = cv2.resize(image, (350, 350))
    return resi_image,i,image

def run():
    st.title("Face Detection using OpenCV")
    activities = ["Webcam", "Upload Image"]
    # st.set_option('deprecation.showfileUploaderEncoding', False)
    st.sidebar.markdown("# Choose Input Source")
    choice = st.sidebar.selectbox("Choose among the given options:", activities)
    # link = '[??Developed by Spidy20](http://github.com/spidy20)'
    # st.sidebar.markdown(link, unsafe_allow_html=True)
    
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    if choice == 'Upload Image':
        st.markdown(
            '''<h4 style='text-align: left; color: #d73b5c;'>* Face Detection is done using Haar Cascade & OpenCV"</h4>''',
            unsafe_allow_html=True)
        img_file = st.file_uploader("Choose an Image", type=['jpg', 'jpeg', 'jfif', 'png'])
        if img_file is not None:
            img = np.array(Image.open(img_file))
            img1 = cv2.resize(img, (350, 350))
            place_h = st.beta_columns(2)
            place_h[0].image(img1)
            st.markdown(
                '''<h4 style='text-align: left; color: #d73b5c;'>* Increase & Decrease it to get better accuracy.</h4>''',
                unsafe_allow_html=True)
            scale_factor = st.slider("Set Scale Factor Value", min_value=1.1, max_value=1.9, step=0.10, value=1.3)
            min_Neighbors = st.slider("Set Scale Min Neighbors", min_value=1, max_value=9, step=1, value=5)
            fd, count, orignal_image = face_detect(img, scale_factor, min_Neighbors)
            place_h[1].image(fd)
            if count == 0:
                st.error("No People found!!")
            else:
                st.success("Total number of People : " + str(count))
                result = Image.fromarray(orignal_image)
                st.markdown(get_image_download_link(result, img_file.name, 'Download Image'), unsafe_allow_html=True)
    if choice == 'Webcam':
        # No 1
        # webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)

        # No 2
        # FRAME_WINDOW = st.image([])
        # cam = cv2.VideoCapture(0)
        # frameWindow(cam, FRAME_WINDOW)

        # No 3
        webrtc_ctx = webrtc_streamer(
            key="WYH",
            mode=WebRtcMode.SENDRECV,
            rtc_configuration=RTC_CONFIGURATION,
            video_processor_factory=VideoProcessor,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=False,
        )
run()