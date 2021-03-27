# -*- coding:utf-8 -*-
# ! usr/bin/env python3
"""
Created on 14/07/2020 上午12:09
@Author: xinzhi yao
"""

from PlantTraitEnrichment import Enrichment

gene_term_file = '../data/Oryzasebase.txt'
obo_file = '../data/to-basic.obo'

Enricher = Enrichment.Gene_Ontology_enrichment(gene_term_file, obo_file)
query_rap_set = {
    'Os01g0382000',
    'Os01g0767900',
    'Os01g0812100',
    'Os02g0521300',
    'Os03g0160100',
    'Os03g0172000',
    'Os05g0368300',
    'Os09g0392100',
    'Os11g0229500',
    'Os11g0482000'}

query_msu_set = {
    'LOC_Os01g28450',
    'LOC_Os01g56200',
    'LOC_Os01g59680',
    'LOC_Os02g32160',
    'LOC_Os03g06410',
    'LOC_Os03g07580',
    'LOC_Os05g30530',
    'LOC_Os09g22450',
    'LOC_Os11g12340',
    'LOC_Os11g29190',
    'LOC_Osp1g00270'}

result_msu = Enricher.ontology_enricement(query_msu_set, id_type='msu', p_threshold=0.05)
result_rap = Enricher.ontology_enricement(query_rap_set, id_type='rap', p_threshold=0.05)
