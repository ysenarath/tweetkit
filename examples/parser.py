import sys
from tweetkit.cmu import ArcTweetNLP

if __name__ == '__main__':
    root_path = sys.argv[1]
    sample_sents = ["Word I'm bout to holla at her via twitter RT @iamJay_Fresh : #trushit - im tryna fucc nicki minaj lol",
                    'To appear (EMNLP 2014): Detecting Non-compositional MWE Components using Wiktionary\
                http://people.eng.unimelb.edu.au/tbaldwin/pubs/emnlp2014-mwe.pdf … #nlproc',
                    'ikr smh he asked fir yo last name so he can add u on fb lololol',
                    ':o :/ :\'( >:o (: :) >.< XD -__- o.O ;D :-) @_@ :P 8D :1 >:( :D =| ") :> ....']
    p = ArcTweetNLP(root_path)
    r = p.parse(sample_sents)
    print(r)
