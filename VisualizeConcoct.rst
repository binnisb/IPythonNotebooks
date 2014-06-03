
.. code:: python

    import os
    import pysam
    import pandas as pd
    import seaborn as sns
    from collections import namedtuple
    from collections import defaultdict
    from collections import Counter
    from glob import glob
.. code:: python

    p = "/home/binni/Programming/uppmax"
    bam_files = glob("{0}/201*/bowtie2_md/*bam".format(p))

.. code:: python

    bams = {}
    for i in bam_files:
        bams[i] = pysam.Samfile( i , "rb" )
    print(bams[i].mapped)

.. parsed-literal::

    23108044


.. code:: python

    reads = defaultdict(Counter)
    for alignedread in bams[i].fetch():
        reads[alignedread.tid].update(alignedread.qname.split("|")[1])


::


    ---------------------------------------------------------------------------
    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-7-e13d7d57515b> in <module>()
          1 reads = defaultdict(Counter)
    ----> 2 for alignedread in bams[i].fetch():
          3     reads[alignedread.tid].update(alignedread.qname.split("|")[1])


    KeyboardInterrupt: 







.. parsed-literal::

    dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 19, 20, 21, 22, 28, 31, 33, 34, 35, 36, 37, 38, 39, 40, 43, 44, 45])



