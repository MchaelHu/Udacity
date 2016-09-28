def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [{"$unwind":"$isPartOf"},
                {"$match":{"country":"India"}},
                {"$group":
                    {   "_id":"$isPartOf",
                        "count" : { "$sum" : 1 } 
                        }
                },
                { "$sort" : { "count" : -1 } },
                { "$limit" : 1 }]
    return pipeline
