# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:29:55 2023

@author: Rutuja Khakare
"""
#pip install elasticsearchquerygenerator

from elasticsearchquerygenerator.elasticsearchquerygenerator import ElasticSearchQuery
import json

def main():
    helper = ElasticSearchQuery(size=100, BucketName="MyBuckets")

    # match phrase
    query=helper.match_phrase(field="myfeild", value="myvalue", operation='must')

    # terms
    query=helper.terms(field="myfeild", value="myvalue", operation='must')

    # Feild Exists
    query = helper.exists(field='comp feild', operation="must")

    #Match
    query=helper.match(field="MMMMM", value="myvalue", operation='must')

    # Geo Queires
    query = helper.add_geoqueries(radius="100", lat="22", lon="33")

    # Aggreation
    helper.add_aggreation(aggregate_name='Duration',field='duration',type='terms',sort='desc', size=3)
   # helper.add_aggreation(aggregate_name="2nd field",field='fiels2',type='terms',sort='desc', size=3)
    #helper.add_aggreation(aggregate_name="ThirdName", field="field3",type='terms',sort='desc', size=3)
    query = helper.complete_aggreation()
    query = helper.query_string(default_field="DEFAULT",query="X OR  Y",operation='must')
    #for aggregation API
    #query = helper.add_geo_aggreation(field="AAAA", lat="22", lon="43",aggregate_name="my_distance")

    print(json.dumps(query, indent=3))


if __name__ == "__main__":
    main()