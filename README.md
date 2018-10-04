# TweetKit
Easy Access Library for Tweet NLP Tools

This module currently support for [CMU ARC TweetNLP](http://www.cs.cmu.edu/~ark/TweetNLP/) only. 
Support for windows is tested, linux will be supported in the near future.

## Tokenizer + Tagger

```
sample_sents = [
'Word I\'m bout to holla at her via twitter RT @iamJay_Fresh : #trushit - im tryna fucc nicki minaj lol',
'To appear (EMNLP 2014): Detecting Non-compositional MWE Components using Wiktionary \
http://people.eng.unimelb.edu.au/tbaldwin/pubs/emnlp2014-mwe.pdf … #nlproc']
p = ArcTweetNLP(root_path)
p.tag(sample_sents)
```

## Dependency Parser

```
sample_sents = [
'Word I\'m bout to holla at her via twitter RT @iamJay_Fresh : #trushit - im tryna fucc nicki minaj lol',
'To appear (EMNLP 2014): Detecting Non-compositional MWE Components using Wiktionary \
http://people.eng.unimelb.edu.au/tbaldwin/pubs/emnlp2014-mwe.pdf … #nlproc']
p = ArcTweetNLP(root_path)
p.parse(sample_sents)
```

## Brown Cluster

```
p = ArcTweetNLP(root_path)
p.get_cluster('goood')
```
