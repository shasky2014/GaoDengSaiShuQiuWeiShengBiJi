import re

in_html = '/Users/neon/PycharmProjects/GaoDengSaiShuQiuWeiShengBiJi/000mulu/mulu_html.txt'
out_data = '/Users/neon/PycharmProjects/GaoDengSaiShuQiuWeiShengBiJi/000mulu/mulu_data.md'
mulu_data = open(out_data, 'w')
mulu_file = open(in_html, 'r')

zhang_jie = []

for line in mulu_file.readlines():
    # if line
    searchObj = re.search('title="(.*?)"', line)
    search_href = re.search('href="(.*?)"', line)
    # if match.group():
    if searchObj:
        title = searchObj.group(1)
        title_no = title[0:3]
        searchObj2 = re.search('\d\d\d(.*?)（(.*?)）', title)
        title_subject = searchObj2.group(1)
        title_subject_no = searchObj2.group(2)

        if title_subject not in zhang_jie:
            zhang_jie.append(title_subject)
            print('###', title_subject)
            mulu_data.writelines('### {}\n'.format(title_subject))

        href = 'https://www.bilibili.com' + search_href.group(1)
        print('##### {0},{1},{2},[{3}]({4})'.format(title_no, title_subject, title_subject_no, title, href))
        mulu_data.writelines('##### [{0}]({1})\n'.format(title, href))
