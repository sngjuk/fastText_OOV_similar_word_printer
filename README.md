# fastText_OOV_similar_word_printer
Can be used to check model's inference performance by entering OOV and seeing similar words. <br>
Note : ./fasttext execution file need be in the same dir. & first model loading is time consuming. (about 2 min)
```
python fast_oov_sim.py [model.bin] [embedding_vector.vec]

In [1]: oov('bicycle')
bicycle
[('bike', 0.8068145513534546), ('tandem', 0.8017247915267944), ('velocipede', 0.7967803478240967), 
('cycle', 0.7866463661193848), ('two-wheeler', 0.7796578407287598), ('wheels', 0.7730188369750977), 
...
... ]

```
Requirements : <br>
- Gensim <br>
<br>
