#!/bin/zsh

CURDIR=$(pwd)

if [  $# = 0 ]; then
    echo "Usage:"
    echo "./test_mergeChunk.sh [INDIR]"
    exit 0
else
    InDir=$(readlink -f $1)
fi

longList=$CURDIR/chunk_list.txt
shortList=$CURDIR/nonchunk_list.txt

if [ -f $longList ]; then
    rm $longList
fi

if [ -f $shortList ]; then
    rm $shortList
fi

find $InDir  -name "*.chunk*.root" -type f -printf "%f\n" | cut -d "." -f1 | sort -u >> $longList

find $InDir  -name "*.root" ! -name "*chunk*" -type f -printf "%f\n" | cut -d "." -f1 | sort -u >> $shortList

