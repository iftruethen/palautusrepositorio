from matchers import And, All, PlaysIn, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self):
        self._matchers = [All()]

    def plays_in(self, team):
        self._matchers.append(PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self._matchers.append(HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self._matchers.append(HasFewerThan(value, attr))
        return self
    
    def build(self):
        return And(*self._matchers)
    
    def one_of(self, *matchers):
        or_matchers = []
        
        for sub_builder in matchers:
            or_matchers.append(sub_builder.build())

        or_matcher = Or(*or_matchers)
        
        self._matchers.append(or_matcher)
        
        return self