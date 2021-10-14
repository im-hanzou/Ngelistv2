# -*- coding: utf-8 -*-
# Written by 3XPL0173R~X3D
# Follow @ github.com/TheChoyon for more scripts
# Special thanks to google cache service
# TeaM_CC (Cyber Commandos)
# If you are a programmer, you can change this code to grab from onholds too!
# Program limitations: If domain name is too large, like the zone-h archive, the domain name is wrapped! I am sorry for that!
import urllib2, re, time, socket
#socket.setdefaulttimeout(30)

def collector(pageUrl, defacer, num):
    target = pageUrl
    try:
        req = urllib2.Request(target, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        data = urllib2.urlopen(req).read()
        l = re.findall('red on [\w.]+ [\w.]+ [\w.]+',data)
        l = l[0].split(' ')
        date = l[2] + ' ' + l[3] + ' ' + l[4]
        print 'Google Cache Date:', date
        domains = re.findall('&lt;td&gt;[\w.-]+',data)
        for i in domains:
            if '.' in i:
                i = i.replace('&lt;td&gt;','')
                print '[' + str(num) + '] http://' + i
                num += 1
                open('zh archive ' + defacer + '.txt', 'a+').write('http://' + i + '\n')
        return num
    except:
        print 'Uh oh! error occured. I assume that it\'s your internet connection that caused this problem!'
        print 'Still skipping, let\'s see if anything we find on the next!'
        return num

def main():
    num = 1
    print 'Zone-H Archive Scanner'
    print 'Coded by 3XPL0173R~X3D'
    defacer = raw_input("Enter Notifier Name: ")
    if defacer == '':
        print 'Are you playing with me? Type in a name!'
        exit(0)
    print 'Notifier Under Observation:', defacer
    print 'Collecting from page: [1]'
    num = collector("http://webcache.googleusercontent.com/search?q=cache:www.zone-h.org/archive/notifier%3D" + defacer + "&num=1&client=opera&hl=en&gl=bd&strip=0&vwsrc=1", defacer, num)
    #time.sleep(2)
    for i in range(2, 51):
        print 'Collecting from page: [' + str(i) + ']'
        num = collector("http://webcache.googleusercontent.com/search?q=cache:www.zone-h.org/archive/notifier%3D" + defacer + "/page=" + str(i) + "&num=1&client=opera&hl=en&gl=bd&strip=0&vwsrc=1", defacer, num)
        #time.sleep(2)
    print 'Total collected domains:', num
    print 'Data is also stored on ', 'zh archive ' + defacer + '.txt'

main()
