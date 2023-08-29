import apache_beam as beam

class SplitRow(beam.DoFn):
  
  def process(self, element):
    # return type -> list
    return  [element.split(',')]
  

class FilterAccountsEmployee(beam.DoFn):
  
  def process(self, element):
    if element[3] == 'Accounts':
      return [element]  
    
class PairEmployees(beam.DoFn):
  
  def process(self, element):
    return [(element[3]+","+element[1], 1)]    
  
class Counting(beam.DoFn):
  
  def process(self, element):
    # return type -> list
    (key, values) = element           # [Marco, Accounts  [1,1,1,1....] , Rebekah, Accounts [1,1,1,1,....] ]
    return [(key, sum(values))]
     

p1 = beam.Pipeline()

attendance_count = (
    
   p1
    |beam.io.ReadFromText('dept_data.txt')
    
    |beam.ParDo(SplitRow())
   # | 'Compute WordLength' >> beam.ParDo(lambda element: [ element.split(',') ]) 

    |beam.ParDo(FilterAccountsEmployee())
    |beam.ParDo(PairEmployees())
    | 'Group ' >> beam.GroupByKey()
    | 'Sum using ParDo' >> beam.ParDo(Counting())  
    
    |beam.io.WriteToText('data/output_new_final')
  
)

p1.run()

# Sample the first 20 results, remember there are no ordering guarantees.
!{('head -n 20 data/output_new_final-00000-of-00001')}