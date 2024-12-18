cat input.txt | grep "[aeiou].*[aeiou].*[aeiou]" | grep "\(.\)\1" | egrep -v "(ab|cd|pq|xy)" | wc -l
cat input.txt |  grep "\(..\).*\1" | grep "\(.\).\1" | wc -l
