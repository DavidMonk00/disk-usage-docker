import pandas as pd
import subprocess

import sys
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO



def parseShellCall():
    output = subprocess.check_output("df").decode("utf-8")
    lines = output.split("\n")
    for i in range(len(lines)):
        line = lines[i].split(" ")
        line = [j for j in line if j]
        lines[i] = line
    return [i for i in lines if i]


def main():
    output = parseShellCall()
    df = pd.DataFrame(output[1:], columns=output[0][:-1])
    df["1K-blocks"] = df["1K-blocks"].astype(int)
    df["Used"] = df["Used"].astype(int)
    df["Available"] = df["Available"].astype(int)
    df = df.drop(columns=["Use%"])
    df["Fraction"] = df.Used/df["1K-blocks"]
    print(df)



if __name__ == '__main__':
    main()
