#Personal Web Page Generator
def main():
    try:
        web=open('suza.html','w')
        name=input("Enter your name:")
        descr=input("Describe yourself:")
        web.write('<html>\n')
        web.write('<head>\n')
        web.write('</head>\n')
        web.write('<body>\n')
        web.write('   <center>\n')
        web.write(f'<h1>{name}<h1>\n')
        web.write('   <center>\n')
        web.write('<hr />\n')
        web.writelines(f'{descr}\n')
        web.write('<hr />\n')
        web.write('</body>\n')
        web.write('</html>\n')
        web.close()
    except Exception as l:
        print(l)
    else:
        print("successifully write web page suza.html")
main()
