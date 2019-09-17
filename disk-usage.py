import pandas as pd
import subprocess
import iphost
import plotly.graph_objects as go
import plotly.express as px
import re

import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO


def parseShellCall():
    output = subprocess.check_output(
        ["ssh", "-o", "StrictHostKeyChecking=no",
         "dmonk@%s" % iphost.get(), "df"]
    ).decode("utf-8")
    lines = output.split("\n")
    disks = []
    for i in range(len(lines)):
        line = lines[i].split(" ")
        line = [j for j in line if j]
        reg = re.match("\/dev\/sd*", lines[i]) or re.match("merger", lines[i])
        if reg or i == 0:
            disks.append(line)
    return [i for i in disks if i]


def generateDataFrame(shell_output):
    df = pd.DataFrame(shell_output[1:], columns=shell_output[0][:-1])
    df["1K-blocks"] = df["1K-blocks"].astype(int)
    df["Used"] = df["Used"].astype(int)
    df["Available"] = df["Available"].astype(int)
    df = df.drop(columns=["Use%"])
    df["Fraction"] = df.Used/df["1K-blocks"]
    return df


def main():
    output = parseShellCall()
    df = generateDataFrame(output)
    print(df)
    fig = px.bar(df, x="Mounted", y="Fraction")
    fig.update_yaxes(range=[0, 1])
    fig.write_html('/plots/index.html')


if __name__ == '__main__':
    main()
