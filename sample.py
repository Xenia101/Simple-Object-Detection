from imageai.Detection import ObjectDetection

detector = ObjectDetection()
model_path = "./models/yolo.h5" # yolo.h5, yolo.tiny.h5
input_path = "./input/sample_img.jpg" # anything you want
output_path = "./output/output.jpg"

detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

print(list(x["name"] for x in detection))
print(list(x["percentage_probability"] for x in detection))
