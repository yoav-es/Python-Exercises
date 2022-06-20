from tabula.io import convert_into
import pandas as pd
import numpy as np

# A function that reads a pdf and convert it's tables into a CSV
def converToCsv(filename):

    convert_into(filename, output_path="output.csv",
                 stream=True, pages="all", guess=True, output_format="csv")
# A function that loads a CSV as DATA
def loadCSV(filename):
    df = pd.read_csv(filename, skiprows=0)
    return df

# A function that calculates the median
def calMedian(data,var):
    df = pd.DataFrame(data)
    M = df[var].median(skipna = True)
    score = (df[var] - M)
    return score

# A function that normalizes one variable by the other.
def normalize(data,var1):
    df = pd.DataFrame(data)
    score = (df[var1] / df['Population\n(1 000)'])
    return score

# A function that calculates sensitivity
def calcSens(data,var1,score):
    df = pd.DataFrame(data)
    score = df['death'] - df[var1]
    return score

# A function that calculates correlation.
def calcluateCorr(first, second):
    return np.corrcoef(first, second)

# A function the calculates the score
def calcVar(score):
    df = pd.DataFrame(score)
    return df.var(skipna=True)

def main():
    # converToCsv('aq.pdf')
    #C0 is the minimal pollution level that can be refrenced as as affecting the heath of humans and causing
    # death and disease
    data = loadCSV('ee_data.csv')
    s1 = calMedian(data, 'NO2')
    s2 = calMedian(data, 'PM2.5')
    s3 = normalize(data, 'C0_10')
    s4 = normalize(data, 'C0_2.5')
    e = calcluateCorr(s1,s2)
    # as it can be seen from the result of 0.18, there is a low correlation between the pollution level
    # in both countries, meaning they spread without depencdency in the atmosphere
    i = calcluateCorr(s3,s4)
    # a correlation coefficient of 0.92 tells us that there is a strong connection between deaths from
    # c02 pollution and death from n02 pollution
    ii = calcluateCorr(s1, s3)
    iii = calcVar(s3)
    iv = calcVar(s4)
    print(iii)
    print(iv)
    # as we can see from the variance in the results, both of them have low variance, meaning
    # they do have similar sensitivities to both pollutants (0.02655-N02, 0.144-PM2.5)

if __name__ == "__main__":
    main()

    # C0 is the minimal background pollution level that could occur naturally or the pollution that
    #can be refrenced as affecting the health of humans and causing negative impact and health issues.
    #i / e
    # as it can be seen from the result of 0.18, there is a low correlation between the pollution level
    # in both countries, meaning they spread without depencdency in the atmosphere
    #ii
    # a correlation coefficient of 0.92 tells us that there is a strong connection between deaths from
    # c02 pollution and death from n02 pollution	\
    #iii
    # as we can see from the variance in the results, both of them have low variance, meaning
    # they do have similar sensitivities to both pollutants (0.02655-N02, 0.144-PM2.5)
