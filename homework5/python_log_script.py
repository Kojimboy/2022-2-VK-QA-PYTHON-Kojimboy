import re

from collections import Counter


def top_methods():
    with open('access.log', 'r') as f:
        log_line = f.readlines()
        method_list = [line.split(' ')[5].strip() for line in log_line]

    uniq_method_sorted = Counter(method_list).most_common()

    with open('py_result.txt', 'a') as f:
        f.write("Total reqs based on method type\n\n")
        f.write('\n'.join('{} {}'.format(x[1], x[0]) for x in uniq_method_sorted))
        f.write("\n")


def top_reqs():
    with open('access.log', 'r') as f:
        log_line = f.readlines()
        url_list = [line.split(' ')[6].strip() for line in log_line]

    uniq_url_sorted = Counter(url_list).most_common()

    with open('py_result.txt', 'a') as f:
        f.write("\nTop 10 most common reqs\n")
        f.write('\n'.join('\n{}\n{}'.format(x[0], x[1]) for x in uniq_url_sorted[0:10]))
        f.write("\n")


def top_big_reqs():
    with open('access.log', 'r') as f:
        log_line = f.read()
        client_error_reqs_list = re.findall(r".* 4\d{2} .*", log_line)
        res_list = [line.split(' ')[9::-10] + line.split(' ')[6::-7] + line.split(' ')[8::-9] + line.split(' ')[:1] for
                    line in client_error_reqs_list]
        for el in res_list:
            el[0] = int(el[0])

        res_list.sort(reverse=True)

    with open('py_result.txt', 'a') as f:
        f.write("\nTop 5 biggest reqs with 4XX code\n")
        f.write('\n'.join('\n{}\n{}\n{}\n{}'.format(x[1], x[2], x[0], x[3]) for x in res_list[0:5]))
        f.write("\n")


with open('py_result.txt', 'w') as f:
    f.write("")

top_methods()
top_reqs()
top_big_reqs()
