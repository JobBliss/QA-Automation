import html
import pandas as pd


def renderresults():
    # to read csv file named "samplee"
    a = pd.read_csv("AutomationQA_Summary.csv")

    # to save as html file
    # named as "showoutput"
    a.to_html("showoutput.html")
    print(a)
    # assign it to a
    # variable (string)
    html_file = a.to_html()
    print(html_file)

if __name__ == '__main__':
    renderresults()

