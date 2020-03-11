# Bachelor Thesis Repo
# Armband
An exercise on gesture recognition using [myo armband](https://www.myo.com) via neural network (tensorflow library).
The exercise start from code of [exelban](https://github.com/exelban/myo-armband-nn)

## Requirement
**Library** | **Version**
--- | ---
**Python** | **^3.5**
**Tensorflow** | **^1.1.0** 
**Numpy** | **^1.12.0**
**sklearn** |  **^0.18.1**
**[myo-python](https://github.com/NiklasRosenstein/myo-python)** |  **it works only with 0.2.2**

You must have installed MYO SDK
```
export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/Users/riccardoberta/Source/GameAI/armband/myo-sdk/myo.framework
```

## Collecting data
64-value array with data from each sensor.
By default myo-python returns 8-value array from each sensors.
Each output return by 2-value array: ```[datetime, [EMG DATA]]```.
64 - value array its 8 output from armband. Just put it to one dimension array.
So you just need to collect 8 values with gesture from armband

```
python3 record.py
```

In repo are collected dataset from Myo armband collected by me. Dataset contains only 5 gestures:
```
- No gesture    (0)
- Fist          (1)
- Ok            (2)
- Viva          (3)
- Gun           (4)
```

## Training network
```sh
python3 train.py
```
75k iteration take about 20 min on GTX 960 or 2h on i3-6100.

## Prediction
### Prediction on data from MYO armband
```sh
python3 predict.py
```
Script will return number (0-5) witch represent gesture (0 - relaxed arm).

### Prediction on training dataset
```sh
python3 predict_train_dataset.py
```
Example output:
```
Accuracy on Test-Set: 98.27% (19235 / 19573)
[2438    5    9    6    4   20] (0) Relax
[   4 2652   45    1    3    9] (1) Ok
[   8   44 4989    1    1    9] (2) Fist
[   8    2    2 4152   28   13] (3) Like
[   2    5    6   27 1839    1] (4) Rock
[  14   22   13   21    5 3165] (5) Spock
 (0) (1) (2) (3) (4) (5)
```

## Model
| **Fully connected 1 (528 neurons)** |
| :---: |
| ReLu |
| **Fully connected 2 (786 neurons)** |
| ReLu |
| **Fully connected 3 (1248 neurons)**  |
| ReLu |
| Dropout |
| **Softmax_linear** |

## Contributors
The implementation and data-gathering processes were conducted by Enrico Casagrande and Alberto Ghiotto with the help and supervision of Prof. Riccardo Berta.
