while read line; do
    echo $line | cut -f -3 -d ' '
done
