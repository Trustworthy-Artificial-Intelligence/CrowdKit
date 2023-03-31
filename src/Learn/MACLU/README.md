# MALC算法说明
该文档将介绍本算法的输入文件中针对多标签主动学习的特殊规范和要求以及本算法中相关函数的定义及使用方法。其中输入文件的通用格式则按照算法库CrowdKit的要求。

## 输入数据集文件规范
本节定义MALC算法输入数据集规范：

- 本算法在多标签二分类场景下进行真值推断和分类的设计，因此每个标签下类别值是从{1,2}中进行选择，类别值为0时表示该样本的标签未被标注。
- 输入数据集包括一小部分标注数据以及大部分未标注数据。并假设在已标注数据中，样本的每个标签都拥有至少一个标注。
- 算法的输入包括.resp文件和.attr文件的路径，.gold文件路径则是可选参数。

## 算法定义
### activelearnerMACLU(in_resp_path,in_attr_path,in_gold_path,instance_num,worker_num,label_num)
输入：
in_resp_path: 工人标注文件路径
in_attr_path：样本特征文件路径
in_gold_path：样本真值文件路径
instance_num：样本总数
worker_num：工人总数
label_num：标签总数
返回一个activelearnerMACLU类实例。

### model.initialize()
初始化函数，用于处理输入文件以及初始化模型参数。

### model.infer()
用于推断有标注样本的聚合标签；对于未标注样本，则训练一个多标签分类器

### model.select_next()
返回一个在下一步需要查询的样本-标签-工人元组。同时也提供每个单独主动学习策略的接口，即样本选择策略select_next_instance()，标签选择策略select_next_label()和工人选择策略select_next_worker()。

### model.update(anno)
输入：
anno：在通过select_next()方法获取样本-标签-工人集合之后，被选工人提供给被选样本的被选标签的标注值。
用于在主动学习策略选择完合适的样本-标签-工人三元组并获取标注后，更新模型数据。

### print_aggregate_accuracy()
输出算法标签集成准确率。

### print_predict_accuracy()
输出算法预测准确率

### print_total_accuracy()
输出算法总准确率（包括标签集成以及预测）