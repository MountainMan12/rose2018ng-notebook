from datapackage import Package
from goodtables import validate
import os

__author__ = 'proccaserra (Philippe Rocca-Serra)'

# author: philippe rocca-serra (philippe.rocca-serra@oerc.ox.ac.uk)
# ontology: http://www.stato-ontology.org

os.chdir('../rose-metabo-JSON-DP-validated')
cwd = os.getcwd()
print("from:", cwd)

dpsch1 = 'rose-aroma-naturegenetics2018-treatment-group-mean-sem-report-datapackage.json'
dpsch2 = 'rose-aroma-science2015-treatment-one-variable-mean-sem-report-datapackage.json'
dpsch3 = 'rose-aroma-science2015-treatment-two-variables-mean-sem-report-datapackage.json'
dpsch4 = 'rose-aroma-data-integration-datapackage.json'

packages = [dpsch1, dpsch2, dpsch3,dpsch4]

file1 = 'rose-aroma-naturegenetics2018-treatment-group-mean-sem-report-table-example.csv'
file2 = 'rose_aroma_science2015_10-1126-aab0696-Table-S3-compounds_only_one_variable.csv'
file3 = 'rose_aroma_science2015_10-1126-aab0696-Table-S1-compounds_only_two_variables.csv'
file4 = 'rose_aroma_compound_science2015_vs_NG2018_data_integration.csv'

files = [file1,file2,file3,file4]

try:
    for counter in range(len(packages)):
        print('json:', packages[counter])
        print('csv:', files[counter])
        try:
            pack = Package(packages[counter])
            pack.valid
            pack.errors
            for e in pack.errors:
                print(e)
            print(pack.profile.name)

            report = validate(files[counter])
            print(report)

        except IOError as e:
            print(e)

except IOError as e:
    print(e)



