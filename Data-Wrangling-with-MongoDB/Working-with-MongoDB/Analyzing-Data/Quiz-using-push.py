def make_pipeline():
    # complete the aggregation pipeline
    pipeline = [
                {"$group":{
                        "_id":"$user.screen_name",
                         "count":{"$sum":1},
                         "tweet_text":{"$push":"$text"}
                            
                             }
                },
                {"$sort":{"count":-1}},
                {"$limit":5}]
    return pipeline
