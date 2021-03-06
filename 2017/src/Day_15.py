import progressbar as pbar


class Generator(object):
    def __init__(self, factor, start_value, multiple_of=1):
        self.factor = factor
        self.value = start_value
        self.divider = 2147483647
        self.multiple_of = multiple_of

    def next(self):
        self.value = (self.factor * self.value) % self.divider
        while self.value % self.multiple_of != 0:
            self.value = (self.factor * self.value) % self.divider
        return bin(self.value)[2:].zfill(32)


bar = pbar.ProgressBar()

gen_a_factor = 16807
gen_a_start = 591
gen_a_multiple = 4
gen_b_factor = 48271
gen_b_start = 393
gen_b_multiple = 8

number_of_pairs_to_check = 5000000

gen_a = Generator(gen_a_factor, gen_a_start, gen_a_multiple)
gen_b = Generator(gen_b_factor, gen_b_start, gen_b_multiple)
count = 0
for i in bar(range(number_of_pairs_to_check)):
    if gen_a.next()[-16:] == gen_b.next()[-16:]:
        count += 1

print("Answer:", count)



