import apache_beam as beam

p = beam.Pipeline()

class AverageFn(beam.CombineFn):
  
  def create_accumulator(self):
     return (0.0, 0)   # initialize (sum, count)

  def add_input(self, sum_count, input):
    (sum, count) = sum_count
    return sum + input, count + 1

  def merge_accumulators(self, accumulators):
    
    ind_sums, ind_counts = zip(*accumulators)       # zip - [(27, 3), (39, 3), (18, 2)]  -->   [(27,39,18), (3,3,2)]
    return sum(ind_sums), sum(ind_counts)        # (84,8)

  def extract_output(self, sum_count):    
    
    (sum, count) = sum_count    # combine globally using CombineFn
    return sum / count if count else float('NaN')
  

small_sum = (
           p 
            | beam.Create([15,5,7,7,9,23,13,5])
            | "Combine Globally" >> beam.CombineGlobally(AverageFn()) 
            | 'Write results' >> beam.io.WriteToText('data/combine')
          )
p.run()

# Sample the first 20 results, remember there are no ordering guarantees.
!{'head -n 20 data/combine-00000-of-00001'}