
# coding: utf-8

# In[4]:

import os
import pysam
import pandas as pd
import seaborn as sns
from collections import namedtuple
from collections import defaultdict
from collections import Counter
from glob import glob


# In[5]:

p = "/home/binni/Programming/uppmax"
bam_files = glob("{0}/201*/bowtie2_md/*bam".format(p))


# In[6]:

bams = {}
for i in bam_files:
    bams[i] = pysam.Samfile( i , "rb" )
print(bams[i].mapped)


# In[7]:

reads = defaultdict(Counter)
for alignedread in bams[i].fetch():
    reads[alignedread.tid].update(alignedread.qname.split("|")[1])


# In[55]:




# In[37]:




# In[5]:



