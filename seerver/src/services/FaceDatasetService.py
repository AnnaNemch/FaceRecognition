import numpy as np
from PIL import Image
import os
import cv2
import sys

# Paths
shared_module_path = 'shared'
data_set_path = shared_module_path + '/dataset'
classifier_path = shared_module_path + '/classifier/haarcascade_frontalface_default.xml'
trainer_path = shared_module_path + '/trainer/trainer.yml'
camera_settings = 1  # TODO :: add to some env settings
photo_count = 40


class FaceDataSetService:

    def __init__(self):
        self.cam = cv2.VideoCapture(camera_settings)
        self.face_detector = cv2.CascadeClassifier(classifier_path)
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

    def collectDataSet(self, face_id):
        print("\n [INFO] Initializing face capture. Look the camera and wait ...")
        # Initialize individual sampling face count
        count = 0
        while True:
            ret, img = self.cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_detector.detectMultiScale(gray, 1.3, 5)  # found faces

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                count += 1
                # Save the captured image into the datasets folder
                cv2.imwrite(data_set_path + "/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
                cv2.imshow('image', img)

            if count >= photo_count:  # Take 30 face sample and stop video
                break

        print("\n [INFO] Exiting Program and cleanup stuff")
        self.cam.release()
        cv2.destroyAllWindows()

    def get_images_and_labels(self, path):
        image_paths = [os.path.join(path, f) for f in os.listdir(path)]
        face_samples = []
        ids = []
        for imagePath in image_paths:
            pil_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_numpy = np.array(pil_img, 'uint8')

            user_id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = self.face_detector.detectMultiScale(img_numpy)

            for (x, y, w, h) in faces:
                face_samples.append(img_numpy[y:y + h, x:x + w])
                ids.append(user_id)

        return face_samples, ids

    def train_faces(self):
        #print("[INFO] Training faces. It will take a few seconds. Wait ...", file=sys.stdout)
        faces, ids = self.get_images_and_labels(data_set_path)
        self.recognizer.train(faces, np.array(ids))

        # Trained model saving
        self.recognizer.write(trainer_path)

        # Print the number of faces trained and end program
        # print("[INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))), file=sys.stdout)
