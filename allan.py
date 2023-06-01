import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
path = r(image)
img = cv2.imread(path)

# Estimate age and gender
results = DeepFace.analyze(img, actions=("gender", "age"))

# Display results
print(results)


# Detect faces
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4,minSize=(30,30))
print("Model Found {0} face(s)!".format(len(faces)))

# Draw rectangles around the faces and display age and gender
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 5)

    # Display age and gender information on the image
    age = results [0]["age"]
    gender = results[0]["gender"]
    label = f"Age: {age}, Gender: {gender}"
    cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()