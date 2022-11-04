#!/bin/bash

echo "Running..........."
spark-submit --master $MASTER --packages $PACKAGES $1
