import apache_beam as beam

class MyTransform(beam.PTransform):
  
  def expand(self, input_coll):
    
    a = ( 
        input_coll
                       | 'Group and sum1' >> beam.CombinePerKey(sum)
                       | 'count filter accounts' >> beam.Filter(filter_on_count)
                       | 'Regular accounts employee' >> beam.Map(format_output)
              
    )
    return a

def SplitRow(element):
    return element.split(',')
  
  
def filter_on_count(element):
  name, count = element
  if count > 30:
    return element
  
def format_output(element):
  name, count = element
  return ', '.join((name.encode('ascii'),str(count),'Regular employee'))

p = beam.Pipeline()

input_collection = ( 
                      p 
                      | "Read from text file" >> beam.io.ReadFromText('dept_data.txt')
                      | "Split rows" >> beam.Map(SplitRow)
                   )

accounts_count = (
                      input_collection
                      | 'Get all Accounts dept persons' >> beam.Filter(lambda record: record[3] == 'Accounts')
                      | 'Pair each accounts employee with 1' >> beam.Map(lambda record: ("Accounts, " +record[1], 1))
                      | 'composite accoubts' >> MyTransform()
                      | 'Write results for account' >> beam.io.WriteToText('data/Account')
                 )

hr_count = (
                input_collection
                | 'Get all HR dept persons' >> beam.Filter(lambda record: record[3] == 'HR')
                | 'Pair each hr employee with 1' >> beam.Map(lambda record: ("HR, " +record[1], 1))
                | 'composite HR' >> MyTransform()
                | 'Write results for hr' >> beam.io.WriteToText('data/HR')
           ) 
p.run()
  
# Sample the first 20 results, remember there are no ordering guarantees.
!{('head -n 20 data/Account-00000-of-00001')}
!{('head -n 20 data/HR-00000-of-00001')}