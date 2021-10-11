import time 
import cv2
from kafka import KafkaProducer, KafkaClient


producer = KafkaProducer(bootstrap_servers="localhost:9092")
topic  = "m-topic"


def video_emitter(video_file):
    # Open the video
    video = cv2.VideoCapture(video_file)
    print("Emitting video file  ....")

    # read the file
    while video.isOpened:
        #read the image in each frame
        success, image = video.read()
        # check if the file has read to the end
        if not success:
            break
        
        # convert the image png
        ret, jpeg = cv2.imencode(".png", image)
        # convert the image to bytes and send to kafka
        producer.send(topic, jpeg.tobytes())
        # To reduce CPU usage create sleep time of 0.2sec  
        time.sleep(0.2)
    # clear the captured video file
    video.release()
    print("Done!!")

if __name__ == "__main__":
    video_emitter("video.mp4")
    


