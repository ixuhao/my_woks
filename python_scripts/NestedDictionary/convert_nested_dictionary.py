from dataset_apollo import apollo

class ComboParser(object):
    def __init__(self, data):
        self.data = data

    def __getattr__(self, key):
        try:
            return ComboParser(self.data[key])
        except TypeError:
            result = []
            for item in self.data.iteritems():
                if key in item:
                    try:
                        result.append(item[key])
                    except TypeError: pass
        return ComboParse(result)

    def __getitem__(self, key):
        return ComboParse(self.data[key])

    def __iter__(self):
        if isinstance(self.data, basestring):
            # self.data might be a str or unicode object
            yield self.data
        else:
            # self.data might be a list or tuple
            try:
                for item in self.data:
                    yield item
            except TypeError:
                # self.data might be an int or fload
                yield self.data

    def __length_hint__(self):
        return len(self.data)

ap = ComboParser(apollo)
print list(ap)
print list(ap.AUDIBLE_PAGE)
print list(ap.AUDIBLE_PAGE.title.appear_threshold)
print list(ap.AUDIBLE_PAGE.title.coordinates)
