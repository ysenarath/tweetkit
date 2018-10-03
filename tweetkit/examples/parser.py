import sys
from tweetkit.cmu import ArcTweetNLP

if __name__ == '__main__':
    root_path = sys.argv[1]
    sample_sents = ['Word I\'m bout to holla at her via twitter RT @iamJay_Fresh : #trushit - im tryna fucc nicki minaj lol',
                    'To appear (EMNLP 2014): Detecting Non-compositional MWE Components using Wiktionary\
                http://people.eng.unimelb.edu.au/tbaldwin/pubs/emnlp2014-mwe.pdf … #nlproc']
    p = ArcTweetNLP(root_path)
    p.parse(sample_sents)
