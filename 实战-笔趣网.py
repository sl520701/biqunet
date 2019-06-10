import requests
from lxml import etree
HEADERS= {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Referer':'https://www.biqukan.net/'
}
def get_detail_url(url):
    Hrefs=[]
    response = requests.get(url,headers = HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    hrefs = html.xpath('//dd[@class="col-md-3"]/a/@href')
    for href in hrefs:
        href = 'https://www.biqukan.net/book/110254/'+href
        Hrefs.append(href)
    return Hrefs
def parse_detail_url(detail_url):
    contents = {}
    content = []
    response = requests.get(detail_url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath('//h1[@class="readTitle"]/text()')
    contents['标题'] = title
    brs = html.xpath('//div[@id="htmlContent"]/text()')
    try:
        brs.remove(brs[0])
    except:
        None
    for each in brs:
        if each.startswith('\r\n                一秒记住'):
            brs.remove(each)
        else:
            each = each.replace('/n','').strip()
            content.append(each)
    contents['正文'] = content
    print(contents)
def spider():
    url = 'https://www.biqukan.net/book/110254/'
    Hrefs = get_detail_url(url)
    for detail_url in Hrefs:
        contents = parse_detail_url(detail_url)
        print(contents)
if __name__ == '__main__':
    spider()