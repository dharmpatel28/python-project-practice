with open("219file1.html","r") as rf:
    with open("219file2.txt",'a') as wf:
        page = rf.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                link_exist = False
            else:
                first_quote = page.find('\"',pos)
                second_quote = page.find('\"', first_quote+1)
                url = page[first_quote+1:second_quote]
                wf.write(url + '\n')
                page = page[second_quote:]   