from mako.template import Template
import glob

filez = sorted(glob.glob("*.mp3"))
t = Template(filename = 'templ.txt')
m3 = t.render(list_of_files = filez)
f = open('music.html', 'w')
f.write(m3)
f.close()

