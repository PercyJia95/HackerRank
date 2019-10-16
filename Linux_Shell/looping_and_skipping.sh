temp=0
while [ $temp -lt 100 ]
do
    if [ $((temp%2)) -eq 1 ];
    then 
        echo "$temp"
    fi
    temp=$((temp+1))
done
