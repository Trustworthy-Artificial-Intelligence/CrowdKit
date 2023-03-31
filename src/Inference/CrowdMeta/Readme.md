# CrowdMeta

## 数据集

### 1. MiniImageNet数据集
MiniImageNet数据集节选自ImageNet数据集。ImageNet是一个非常有名的大型视觉数据集，它的建立旨在促进视觉识别研究。训练ImageNet数据集需要消耗大量的计算资源。ImageNet为超过1400万张图像进行了注释，而且给至少100万张图像提供了边框。ImageNet包含2万多个类别，每个类别均有不少于500张图像。

训练这么多图像需要消耗大量的资源，因此在2016年google DeepMind团队Oriol Vinyals等人在ImageNet的基础上提取出了MiniImageNet数据集。如果您在工作中使用MiniImageNet数据集，请引用以下论文。

```
@inproceedings{Vinyals2016,
	author = {Vinyals, Oriol and Blundell, Charles and Lillicrap, Timothy and Kavukcuoglu, Koray and Wierstra, Daan},
	title = {Matching networks for one shot learning},
	year = {2016},
	booktitle = {NIPS},
	pages = {3637--3645},
	numpages = {9},
}
```

MiniImagenet一共有2.86GB，文件架构如下：

 root/ &nbsp;  
 &emsp;  |- images/  
 &emsp; &emsp; |- n0153282900000005.jpg   
 &emsp; &emsp; |- n0153282900000006.jpg  
 &emsp; &emsp; |- …  
 &emsp; |- train.csv   
 &emsp; |- test.csv  
 &emsp; |- val.csv  

数据集可从[github](https://github.com/yaoyao-liu/mini-imagenet-tools)仓库下载。

### 2. Omniglot数据集
Omniglot Dataset翻译过来就是全语言文字数据集，包含各种语言的不同字母表，如日语的平假名，日语的片假名，韩语的元音和辅音，最常见的拉丁字母等。Omniglot Dataset共包含50个不同语言的字母表，每个字母表中包含不同的字符，共1623种字符，每个字符有20个不同的人书写。也就是说Omniglot Dataset数据集包含1623个类，每个类有20个训练数据。如果您在工作中使用Omniglot数据集，请引用以下论文。
```
@article{Omniglot,
	author = {Brenden M. Lake  and Ruslan Salakhutdinov  and Joshua B. Tenenbaum },
	title = {Human-level concept learning through probabilistic program induction},
	journal = {Science},
	volume = {350},
	number = {6266},
	pages = {1332-1338},
	year = {2015},
	doi = {10.1126/science.aab3050},
}
```
可以从Omniglot数据集[github](https://github.com/brendenlake/omniglot)仓库下载。下载仓库后分别提供了python和matlab的api，下载并解压python目录文件下的`images_background.zip`和`images_evaluation.zip`，其为数据集划分的训练数据和测试数据。

## 运行
目录下代码功能为：

learner.py  网络搭建  
meta.py  网络训练  
MiniImagenet.py  miniimagenet  数据加载  
miniimagenet_train.py  训练与finetunin  
omniglot.py  omniglot  数据加载  
omniglot_train.py  训练与finetuning  
meanstd.py  特征分布提取  
infer.py  真值推断  

注：因miniimagenet数据集与omniglot数据结构略有不同，所以其数据加载略有不同，如若要使用其他数据集，建议将数据文件结构预处理为miniimagenet数据集相同结构。训练与finetuning文件`miniimagenet_train.py`与`omniglot_train.py`本质上没有区别，只在调用数据加载上有所差异。
### 1. 预训练模型+finetuning
运行miniimagenet_train.py文件，获得高阶特征表示。
```bash
#python method.py
python miniimagenet_train.py
```
### 2. 特征分布提取
运行meanstd.py文件，提取目标任务的特征分布。目标任务dataset.txt存放任务图片的地址。
```bash
#python method.py <目标任务地址> <特征分布地址>
python meanstd.py dataset.txt distribution.txt
```
### 3. 真值推断
运行infer.py文件，得到最终的集成标签文件以及准确率。
```bash
#python method.py <.resp地址> <.gold地址> <高阶特征地址> <特征分布地址>
python infer.py label.resp truth.gold feature.attr distribution.txt
```