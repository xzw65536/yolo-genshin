# yolo-genshin
our results on video detection are in output folder
we use colab to train our model, here are the instructions:
1. open a new notebook on colab
2. Enter the following code to do the train process:
    !git clone https://github.com/xzw65536/yolo-genshin.git
    !python ./yolo-genshin/data/makeTxt.py
    !python ./yolo-genshin/data/voc_label.py
    !python ./yolo-genshin/train.py
3. Enter the following code to do the detect process, put test file under the /test folder.
    !python ./yolo-genshin/detect.py
