import requests
from bs4 import BeautifulSoup
import time
print("write the wikipedia link") #for example water
input_link = input()
already_visited = set(input_link)  # for not repeating links  

print(input_link)

def remove_brackets(html): 
    """
    Remove everything between brackets,
    except brackets in between <html tag> 
    """
    outstr = ""

    round_brackets = 0 
    angle_brackets = 0 

    for ch in html:             #ch is a character width 
        if round_brackets < 1:  #not between brackets    #round brackets--> ()
            if ch == "<":
                angle_brackets += 1               #angle brackets--> <>
            elif ch == ">":
                angle_brackets -= 1

            outstr += ch
            

        if angle_brackets < 1:
            if ch == "(":
                round_brackets += 1

            if round_brackets == 0 and round_brackets >= 1: 
                outstr += ch

            if ch == ")":
                round_brackets -= 1


    return outstr

while input_link != "Philosophy":  #if input_link or word not equal philosophy 
    r = requests.get("http://en.wikipedia.org/wiki/{}".format(input_link))  #download html and save it as string text
    soup = BeautifulSoup(r.content, "lxml")

    index = 0
    while True:
        x = soup.select("div.mw-parser-output")[0].decode_contents(formatter="lxml")
        s = BeautifulSoup(remove_brackets(x) , "lxml")

        input_link = s.select("p a")[index]["href"].replace("/wiki/", "")
        
        if ":" in input_link or "#" in input_link:
            index += 1
            continue

        break
    time.sleep(0.5)
    print(input_link)

    if input_link in already_visited:
    	break
    already_visited.add(input_link)

