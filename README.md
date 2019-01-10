# words_vectors_embeddings

## 1. 数据处理
  
    1.1. 将待训练词向量的文件将demo.txt进行替换; 然后修改data_process.py 文件中的文件名
   
    1.2. 运行data_process.py 文件; 完成待训练文件的预处理; 生成word.txt 文件
        运行命令: python data_process.py
      
### 2. 词向量训练 
    2.1 修改train.py文件中 run('fasttext')方法中传入的参数;
        使用Word2vec方法训练, 参数传入 'word2vec'; 
        使用fasttext方法训练, 参数传入 'fasttext';
       
     2.2 运行train.py文件; 在ckpt文件夹中对应方法文件夹中生成响应的model模型
        运行命令: python train.py
    
### 3.词向量的测试
     3.1  obj = Test('word2vec') 类里面传入训练词向量模型的方法, 
         依test.py文件 main方法 中提供的方式自己想要的词向量,
     3.2  运行test.py, 获取词向量的近义词或者词向量
         命令: python test.py
   
### 4. 相关命令解说：
        model 可以为实例的word2vec或者 fasttext类
        
        获取词向量及近似词的方法如下：
        print('词表长度：', len(model.wv.vocab))
        print('爱    对应的词向量为：', model['爱'])
        print('喜欢  对应的词向量为：', model['喜欢'])
        print('爱  和  喜欢的距离（余弦距离）', model.wv.similarity('爱', '喜欢'))
        print('爱  和  喜欢的距离（欧式距离）', model.wv.distance('爱', '喜欢'))
        print('与 爱 最相近的3个词：', model.wv.similar_by_word('爱', topn=3))
        print('与 喜欢 最相近的3个词：', model.wv.similar_by_word('喜欢', topn=3))
        print('爱，喜欢，恨 中最与众不同的是：', model.wv.doesnt_match(['爱', '喜欢', '恨']))
