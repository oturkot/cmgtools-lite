#! /bin/bash

if [[ $@ ]]; then
  OUTPUT="result.root"
  hadd -f -T $OUTPUT $@ && echo "hadd done"
  python dumpCountsFromHist.py $OUTPUT
else
  echo "No input files given."
fi

