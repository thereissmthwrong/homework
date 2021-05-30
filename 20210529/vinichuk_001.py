from mako.template import Template
import glob

f = open('m3u_template.m3u', 'w')
f.write('''#EXTM3U
% for i in list_of_files:
#EXTINF:123, File1
${i}
%endfor
''')
f.close()

filez = sorted(glob.glob("*.mp3"))
t = Template(filename = 'm3u_template.m3u')
m3 = t.render(list_of_files = filez)
f = open('play.m3u', 'w')
f.write(m3)
f.close()
