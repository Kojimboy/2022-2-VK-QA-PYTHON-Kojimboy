> result.txt
echo "Общее число запросов" >> result.txt
wc -l < access.log >> result.txt
echo >>result.txt | echo "Общее количество запросов по типу" >> result.txt
cat access.log | awk '{print $6}' | sort | uniq -c | sort -nr >> result.txt
echo >>result.txt | echo "Топ 10 самых частых запросов" >> result.txt
cat access.log | cut -d " " -f 7  | sort | uniq -c | sort -nr | head -n 10  | awk '{print $2, "\n" $1}' >> result.txt
echo >>result.txt | echo "Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой" >> result.txt
cat access.log | awk '$9 ~/4./' | sort -k10 -nr | head -n 5 | awk '{print $7, "\n" $9, "\n" $10, "\n" $1}'  >> result.txt
echo >>result.txt | echo "Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой" >> result.txt
cat access.log | awk '$9 ~/5./' | awk '{print $1}' | uniq -c | sort -nr| head -n 5 | awk '{print $2, "\n" $1}' >> result.txt

