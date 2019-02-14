import re

in_html = '/Users/light/PycharmProjects/untitled1/gaodengdaishu_qiuweisheng/gd000_mulu/mulu_html.txt'
out_data = '/Users/light/PycharmProjects/untitled1/gaodengdaishu_qiuweisheng/gd000_mulu/mulu_data.txt'
mulu_data = open(out_data, 'w')
mulu_file = open(in_html, 'r')
for line in mulu_file.readlines():
    # if line
    searchObj = re.search('title="(.*?)"', line)
    # if match.group():
    if searchObj:
        title = searchObj.group(1)
        title_no = title[0:3]
        searchObj2 = re.search('\d\d\d(.*?)（(.*?)）', title)
        title_subject = searchObj2.group(1)
        title_subject_no = searchObj2.group(2)
        mulu_data.writelines('{0},{1},{2},{3}\n'.format(title_no, title_subject, title_subject_no, title))
        print(title_no, title_subject, title_subject_no, title)
