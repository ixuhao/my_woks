from dataset_apollo import apollo

class PageStruct(object):
    def __init__(self, entries):
        for key, value in entries.iteritems():
            value2 = (PageStruct(value) if isinstance(value, dict) else value)
            setattr(self, key, value2)

    def __repr__(self):
        """"""
        attrs = str([x for x in dir(self) if '__' not in x])
        return "<DictToObj>: %s" % attrs

ap = PageStruct(apollo)
print ap
print ap.AUDIBLE_PAGE
print ap.AUDIBLE_PAGE.title.appear_threshold

