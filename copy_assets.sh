while read line
do
    cp -r $line pyz-dist/
done < assets.txt
