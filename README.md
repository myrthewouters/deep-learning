# Fine-tuning of Pre-trained Deep Networks for Bone Age Assessment

This repository is part of a project for a deep learning course, in which the RNSA Bone Age dataset is used, available at [Kaggle](https://pubs.rsna.org/doi/full/10.1148/radiol.2017170236). The aim of the project was to experiment with fine-tuning of pre-trained networks, including both image and gender input for bone age assessment. 

## Dataset
Original images were resized to 256x256 pixels with padding. Code for resizing and padding can be found in the *preprocessing* directory. Additionally, real-time data augmentation on the training set is used during training. An example image can be found below.


<table class="tg">
<thead>
  <tr>
    <th class="tg-0lax">Original</th>
    <th class="tg-0lax">Padded</th>
    <th class="tg-0lax">Augmented</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0lax"><img src="https://github.com/myrthewouters/deep-learning/blob/master/example-images/9140-original.png" height="200"></td>
    <td class="tg-0lax"><img src="https://github.com/myrthewouters/deep-learning/blob/master/example-images/9140-resized-padded.png" height="200"></td>
    <td class="tg-0lax"><img src="https://github.com/myrthewouters/deep-learning/blob/master/example-images/9140-augmented.png" height="200"></td>
  </tr>
</tbody>
</table>

## Methods
The model used in this project incorporates a fine-tuned pre-trained architecture (VGG16 or ResNet18) to handle the image input and a gender network. A schematic overview of the model can be found below.

<img src="https://github.com/myrthewouters/deep-learning/blob/master/schematic-model.png" width="400
">

The following architectures pre-trained on the ImageNet dataset were used: [VGG16](https://keras.io/api/applications/vgg/#vgg16-function) and [ResNet18](https://github.com/qubvel/classification_models). Next to the model architecture provided above, I trained two modes (VGG16 and ResNet18) on image input only.

Training, tuning and evaluation procedures for the models including both gender and image inputs as shown schematically are presented in the following notebooks: *notebooks/vgg16-concatenated.ipynb* and *resnet18-concatenated.ipynb* and together form the majority part of this project. 

Additionally, training and evaluation for the models including image input only can be found in the following notebooks: *notebooks/vgg16.ipynb* and *notebooks/resnet18.ipynb*. These models are trained with optimal hyperparameters found for the models including both gender and image inputs, instead of being separately tuned.

Note: to run the notebooks on the ResNet18 models, please install the following keras patch (pip install -U --force-reinstall --no-dependencies git+https://github.com/datumbox/keras@bugfix/trainable_bn) and tensorflow 1.14, due to issues on finetuning of pre-trained models including batch normalization layers. Read more [here](https://github.com/keras-team/keras/pull/9965). The notebooks on the VGG16 models can be run on Keras 2.2.4 and tensorflow 2.2.

## Results

The table below presents the validation and test MAE in months for the models with optimal hyperparameter settings. Details on the optimal hyperparameter settings can be found in the accompanying notebooks in the *notebooks* directory. The best-performing model is the model incorporating the ResNet-18 architecture, including both image and gender inputs. 

<table class="tg">
<thead>
  <tr>
    <th class="tg-baqh">Model</th>
    <th class="tg-baqh" colspan="4">MAE (months)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-baqh"></td>
    <td class="tg-wrh3" colspan="2"><span style="font-weight:bold">Image + gender input</span></td>
    <td class="tg-chp3" colspan="2">Image input only</td>
  </tr>
  <tr>
    <td class="tg-baqh"></td>
    <td class="tg-baqh">Val</td>
    <td class="tg-baqh">Test</td>
    <td class="tg-ay88">Val</td>
    <td class="tg-t87r">Test</td>
  </tr>
  <tr>
    <td class="tg-0qqg">VGG16 (finetuned)</td>
    <td class="tg-0qqg">10.6</td>
    <td class="tg-0qqg">15.9</td>
    <td class="tg-ay88">12.1</td>
    <td class="tg-ay88">16.9</td>
  </tr>
  <tr>
    <td class="tg-0qqg">ResNet18 (finetuned)</td>
    <td class="tg-0qqg">10.6</td>
    <td class="tg-0qqg">11.7</td>
    <td class="tg-ay88">12.8</td>
    <td class="tg-ay88">14.6</td>
  </tr>
</tbody>
</table>
