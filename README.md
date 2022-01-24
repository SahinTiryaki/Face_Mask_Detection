# Face-Mask-Detection
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The covid19 virus influence negatively our life since 2019 and the virus the first appearance place in the world was Wuhan city in China, and then spread all over world,from this moment we have to wear a face maske in crowded places such as cafe, restaurant.. While wearing mask is not the ultimate solution, it still reduces the rate of transmission of the virus.In addition much applications were produced by software developers. I devoloped this project to solve face mask problem.</p>
in this project, following process is adopted <br>

<ul>
  <li>Prepare mask and without mask images for classifiying model</li>
  <li> Frezee the all layers (without first layer) of VGG19 and add dense,change output layer </li>
    <li> Train the classifier to classify faces into mask or non-mask labels. </li>
  <li> Detect Face with Opencv Haar Cascade Classifier </li>
  <li> Classifiy Face with Pretrained VGG19 model </li>
  </ul>
 
## Dataset
you can reach dataset from this url: https://www.kaggle.com/ashishjangra27/face-mask-12k-images-dataset
![Ekran Görüntüsü 2021-05-26 13-20-24](https://user-images.githubusercontent.com/59391291/119644110-30febb80-be25-11eb-9697-d0c6115ddeb2.png)
![Ekran Görüntüsü 2021-05-26 13-21-39](https://user-images.githubusercontent.com/59391291/119644233-512e7a80-be25-11eb-9070-223b8f128d7c.png)
## Model
<li>loss: binary cross entropy</li>
<li>metric: accuracy</li>

![Ekran Görüntüsü 2021-05-26 13-24-14](https://user-images.githubusercontent.com/59391291/119644582-acf90380-be25-11eb-9e1e-426dd2ccaf9e.png)
![Ekran Görüntüsü 2021-05-26 13-25-30](https://user-images.githubusercontent.com/59391291/119644720-dca80b80-be25-11eb-89c7-8517311ee7d4.png)

## Demo

https://user-images.githubusercontent.com/59391291/150820734-5cdfd81d-9c10-4d18-8ca7-ade1aa18e995.mp4

