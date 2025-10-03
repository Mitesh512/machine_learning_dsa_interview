"""
User Trend Analytics
input: user_interaction per minute, as a stream ---> list(int)

def mov_avg(x):
    pass

output: just moving avg for x mins sum(past x mins) /x

"""

def get_stream():
    stream = [12344,1234,123,4523,5678,1234]
    return stream

class Moving_avgs:
    def __init__(self,n_wind):
        self.n_wind = n_wind
        self.stream = get_stream()
        self.wind_sum = sum(self.stream[-self.n_wind:])
    
    def add_to_stream(self,user_freq):
        self.new_ele = user_freq
        self.n_wind_min_1= self.stream[-self.n_wind]
        # remove the n_win -1 ele and add new element in moving sum
        self.wind_sum -= self.n_wind_min_1
        self.wind_sum += user_freq
        # update stream
        self.stream.append(user_freq)
        
    def get_moving_avgs(self):
        return round(self.wind_sum / self.n_wind,4)


print(sum([5678,1234,345])/3) # test case
n_wind = 3
moving_avgs = Moving_avgs(n_wind)
for strm in [12,34,46,32,45]:
    moving_avgs.add_to_stream(strm)
    print(moving_avgs.stream)
    print(moving_avgs.get_moving_avgs())


"""
from collections import defaultdict

class PopularityTracker:
    def __init__(self):
        self.id_to_count = defaultdict(int)
        self.count_to_ids = defaultdict(set)
        self.max_count = 0

    def increase(self, id):
        old_count = self.id_to_count[id]
        new_count = old_count + 1
        self.id_to_count[id] = new_count

        # Remove from old count set
        if old_count > 0:
            self.count_to_ids[old_count].discard(id)
            if not self.count_to_ids[old_count]:
                del self.count_to_ids[old_count]

        # Add to new count set
        self.count_to_ids[new_count].add(id)

        # Update max_count
        if new_count > self.max_count:
            self.max_count = new_count

    def decrease(self, id):
        if id not in self.id_to_count:
            return

        old_count = self.id_to_count[id]
        if old_count == 0:
            return

        new_count = old_count - 1
        self.id_to_count[id] = new_count

        # Remove from old count set
        self.count_to_ids[old_count].discard(id)
        if not self.count_to_ids[old_count]:
            del self.count_to_ids[old_count]
            # Update max_count if needed
            if old_count == self.max_count:
                self.max_count -= 1
                while self.max_count > 0 and self.max_count not in self.count_to_ids:
                    self.max_count -= 1

        # Add to new count set if > 0
        if new_count > 0:
            self.count_to_ids[new_count].add(id)

    def get_most_popular(self):
        if self.max_count == 0:
            return None
        return next(iter(self.count_to_ids[self.max_count]))


"""




