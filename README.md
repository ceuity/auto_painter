# Auto-Painter

- [Auto-painter: Cartoon Image Generation from Sketch by Using Conditional Generative Adversarial Networks](https://arxiv.org/abs/1705.01908)

## Abstract

최근에, DNN을 사용한 사실적인 이미지 생성은 머신러닝과 컴퓨터 비전 분야에서 화제가 되고 있다. 대량의 이미지를 학습함으로써 이미지는 픽셀 수준에서 생성될 수 있다. 흑백 스케치부터 다채로운 만화 이미지를 생성하는 방법을 배우는 것은 흥미로운 연구 주제일 뿐만 아니라, 디지털 엔터테이먼트의 잠재적 활용 분야이기도 하다. 우리는 이 논문에서 cGAN을 이용하여 스케치를 이미지로 합성하는 문제에 대해 조사한다. 우리는 스케치와 호환되는 색상을 자동으로 생성해주는 오토 페인터 모델을 제안한다. 새로운 모델은 손으로 그린 스케치에 적절한 색을 칠해주는 것이 가능할 뿐만 아니라, 사용자가 선호하는 색상을 나타낼 수도 있다. 두 개의 스케치 데이터셋 실험 결과는 오토 페인터가 현존하는 image-to-image 방법보다 더 잘 작동하는 것을 보여준다.

![images00](./images/images00.png)

## Related Work

- Generative Adversarial Networks(GANs)
- Conditional GANs
- Image-to-Image

## Method

- Supervised Learning
    - Dataset : sketch-colored pairs image set

### Network Structure

- U-Net
- Discriminator : PatchGAN

![images01](./images/images01.png)

### Loss Function

- Generator Loss

![](https://latex.codecogs.com/svg.image?L_G&space;=&space;\mathbb{E}_{x\sim&space;pdata(x),&space;z\sim&space;pdata(z)}[log(1&space;-&space;D(x,&space;G(x,&space;z)))])

- Pixel-level loss

![](https://latex.codecogs.com/svg.image?L_p&space;=&space;\mathbb{E}_{x,&space;y\sim&space;pdata(x,&space;y),&space;z&space;\sim&space;pdata(z)}[\parallel{y&space;-&space;G(x,&space;z)}\parallel_1])

- Extracted high-level feature from VGG loss

![](https://latex.codecogs.com/svg.image?L_f&space;=&space;\mathbb{E}_{x,&space;y\sim&space;pdata(x,&space;y),&space;z&space;\sim&space;pdata(z)}[\parallel{\phi(y)&space;-&space;\phi&space;G(x,&space;z)}\parallel_2])

- Total variation loss

![](https://latex.codecogs.com/svg.image?L_%7Btv%7D%20=%20%5Csqrt%7B(y_%7Bi&plus;1,%20j%7D%20-%20y_%7Bi,%20j%7D)%5E2%20&plus;%20(y_%7Bi,%20j&plus;1%7D%20-%20y_%7Bi,%20j%7D)%5E2%7D)

- Total Loss Function

![](https://latex.codecogs.com/svg.image?L&space;=&space;w_pL_P&space;&plus;&space;w_fL_f&space;&plus;&space;w_GL_G&space;&plus;&space;w_{tv}L_{tv})

## Experimental Studies

- Dataset
    - 512x512 pixel Minions 1100 pictures
    - 512x512 pixel Japanimation 60000 pictures
    - Generate sketch image using XDoG filter

## 문제점들

- sketch와 colored 이미지의 위치가 바뀌는 경우가 있어서 이미지를 불러올 때 position을 argument로 하여 위치를 지정할 수 있게 했었는데 [tf.Dataset.map](http://tf.Dataset.map) 함수를 적용할 때 arguement를 지정할 수 없어서 map 함수에 lambda 식과 tf.py_function 함수를 이용하여 해결하였다.
