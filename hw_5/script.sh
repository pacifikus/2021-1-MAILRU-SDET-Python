#!bin/bash
file=$1
if [ -z $dirpath ]
then 
	echo "total count" > result.txt
	cat $file | wc -l >> result.txt
	
	echo "" >> result.txt
	echo "total by type" >> result.txt
	methods=$(cat $file | awk 'length($6)<10{print substr($6,2)}' | sort | uniq)
	for n in $methods
    do
        (echo -e "$n - \c"; cat $file | grep -w $n | wc -l) >> result.txt
    done

	echo "" >> result.txt
	echo "total 10 most frequent" >> result.txt
    cat $file | awk '{print $7}' | sort | uniq -c | sort -rn | head -10 >> result.txt
	
	echo "" >> result.txt
	echo "top 5 4XX requests" >> result.txt
    cat $file | awk 'int($9/100)==4 {print $1,$9,$7,$10}' |  sort -rnk4 | head -n 5 >> result.txt
	
	echo "" >> result.txt
	echo "top 5 5XX requests" >> result.txt
    cat $file | awk 'int($9/100)==5 {print $1}' | sort | uniq -c | sort -rn | head -5 >> result.txt
fi
