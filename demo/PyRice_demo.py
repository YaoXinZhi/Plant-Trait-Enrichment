# -*- coding:utf-8 -*-
# ! usr/bin/env python3
"""
Created on 10/07/2020 下午12:19
@Author: xinzhi yao
"""
from pyrice.multi_query import MultiQuery
import time
import csv
from pyrice.utils import search
from pyrice import utils
from multiprocessing import cpu_count
from argparse import ArgumentParser
from pyrice.build_dictionary import update_gene_dictionary, update_local_database
import pandas as pd
from pandasql import sqldf

'''
Database_name: keywords
    Oryzabase : oryzabase
    RapDB : rapdb
    Gramene : gramene
    IC4R : ic4r
    SNP-Seek : snpseek
    Funricegene : funricegene_genekeywords, funricegene_faminfo, funricegene_geneinfo
    MSU : msu
    EMBL-EBI Expression Atlas : embl_ebi
    GWAS-ATLAS : gwas_atlas
    Planteome : planteome


'''




# utils.chrome_path = "/usr/bin/chromedriver"
utils.chrome_path = '/usr/local/share/chromedriver'

# fixme: Search gene by potision on chromosome
query = MultiQuery()
result = query.search_on_chromosome(chro="chr01", start_pos="1",
                                    end_pos="20000", number_process=4, dbs="all", save_path="../result/")
print("Output database:", result)

# fixme: Query gene by chromosome
query = MultiQuery()
result = query.query_by_chromosome(chro="chr01", start_pos="1", end_pos="20000",
                                   number_process = 4, multi_processing=True,
                                   multi_threading=True, dbs="all")

query.save(result, save_path="../result/",
           format=["csv", "html", "json", "pkl"], hyper_link=False)
print("Output database:", result)

# fixme: Query gene using id, loc or iric
from pyrice.multi_query import MultiQuery

query = MultiQuery()
result = query.query_by_ids(ids=[ "Os08g0164400", "Os07g0586200" ],
                            locs=[ "LOC_Os10g01006", "LOC_Os07g39750" ],
                            irics=[ "OsNippo01g010050", "OsNippo01g010300" ],
                            number_process=4, multi_processing=True, multi_threading=True, dbs="all")
query.save(result, save_path="../result/",
           format=[ "csv", "html", "json", "pkl" ], hyper_link=False)
print("Output database:", result)

# fixme: Query for new attributes on new databases
query = MultiQuery()
result = query.query_new_database(atts=[ 'AT4G32150' ], number_process=4,
                                  multi_processing=True, multi_threading=True, dbs=[ 'planteome' ])
query.save(result, save_path="../result/",
           format=["csv", "html", "json", "pkl"], hyper_link=False)
print("Output database:", result)


