# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:03:55 2023

@author: Andres
"""

import apache_beam as beam

p2 = beam.Pipeline()

lines = (
            p2
            | beam.Create([
               'Using create transform ',
               'to generate in memory data ',
               'This is 3rd line ',
               'Thanks '])
     
            | beam.io.WriteToText('data/outCreate1')
          )
p2.run()  

# visualize output
!{('head -n 20 data/outCreate1-00000-of-00001')}

-------------------------------------------

import apache_beam as beam

p3 = beam.Pipeline()

lines1 = (p3
           
           | beam.Create([1,2,3,4,5,6,7,8,9])
           
           | beam.io.WriteToText('data/outCreate2')
          )
p3.run()

# visualize output
!{('head -n 20 data/outCreate2-00000-of-00001')}

-------------------------------------------------

import apache_beam as beam

p4 = beam.Pipeline()


lines = (p4
           | beam.Create([("maths",52),("english",75),("science",82), ("computer",65),("maths",85)])
         
            | beam.io.WriteToText('data/outCreate3')
          )
p4.run()

# visualize output
!{('head -n 20 data/outCreate3-00000-of-00001')}

----------------------------------------------------------------

import apache_beam as beam

p5 = beam.Pipeline()

lines = ( p5
         
       | beam.Create({'row1':[1,2,3,4,5],
                     'row2':[1,2,3,4,5]})
       | beam.Map(lambda element: element)
       | beam.io.WriteToText('data/outCreate4')
  )
  
p5.run()

# visualize output
!{('head -n 20 data/outCreate4-00000-of-00001')}



