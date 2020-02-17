# Simple Object Detection

Simple Object Detection in python

## USAGE

1. download models [**yolo.h5** - YOLOv3](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5)

2. Save the file in ./models

3. Add to path

```python 
model_path = "./models/yolo.h5"
```

4. Name the input/output file name

```python
input_path = "./input/input.jpg"
output_path = "./output/output.jpg"
```

5. Run

## EXAMPLE

Load Model & Detection

```python
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)
```

Print percentage_probability & name of object

```python
print(list(x["name"] for x in detection))
print(list(x["percentage_probability"] for x in detection))
```

Intput

<p align=center>
  <img width="50%" src="https://github.com/Xenia101/Simple-Object-Detection/blob/master/input/sample_img.jpg?raw=true">
</p>

Output

<p align=center>
  <img width="50%" src="https://github.com/Xenia101/Simple-Object-Detection/blob/master/output/output.jpg?raw=true">
</p>
