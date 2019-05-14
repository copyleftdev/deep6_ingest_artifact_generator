
import random
site_ids = [11111111,22222222,33333333,44444444,
               55555555,66666666,77777777,88888888,99999999]


def seed_site_id(source_index,destination_index, site_id):
    root = {}
    source = {"source": {"index": source_index}}
    desitination = {"dest": {"index": destination_index}}
    script = {"script":{"source": random.choice(site_ids)}}
    root.update(source)
    root.update(desitination)
    root.update(script)
    print(root)



seed_site_id("same1", "same2", 1)
"
String[] sids = new String[] {"11111111","22222222","33333333","44444444",
               "55555555","66666666","77777777","88888888","99999999"};


