# fastText_OOV_similar_word_printer
Used to check model's inference performance by entering OOV(Out of vocabulary) and seeing similar words. <br>
Note : It needs be in the same dir with fasttext execution file. & It takes some time to load model loading (~3 min)
```
python fast_oov_sim.py [model.bin] [embedding_vector.vec]

In [1]: oov('bicycle')
bicycle
[('bike', 0.8068145513534546), ('tandem', 0.8017247915267944), ('velocipede', 0.7967803478240967), 
('cycle', 0.7866463661193848), ('two-wheeler', 0.7796578407287598), ('wheels', 0.7730188369750977), 
...
... ]
In [2]: oov('cat')
cat
[('bobcat', 0.9520692639593045), (... ]

```
Requirements : <br>
- fastText <br>
- Gensim <br>
<br>
