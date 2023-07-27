#!/bin/bash
BATCHFILE="data/NIFTI/batch.csv"
OUTPUTDIR="output"
LOGDIR="log"
#VERBOSITY="5"
CONFIGFILE="config/base"
TYPES="nw;lw;mw"

for TYPE in $(tr ";" "\n" <<< "$TYPES"); do
    pyradiomics $BATCHFILE -p "$CONFIGFILE"_$TYPE.yaml -f csv \
    -o "$OUTPUTDIR/fe-$TYPE.csv" \
    --log-file "$LOGDIR/fe-$TYPE.log" \
    --logging-level DEBUG \
    -j 2
done
