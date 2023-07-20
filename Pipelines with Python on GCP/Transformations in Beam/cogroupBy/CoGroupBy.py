# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 23:08:04 2023

@author: Andres
"""

import apache_beam as beam

def retTuple(element):
  
  thisTuple=element.split(',')
  return (thisTuple[0],thisTuple[1:])
                
p1 = beam.Pipeline()

# Apply a ParDo to the PCollection "words" to compute lengths for each word.
dep_rows = ( 
                p1
                | "Reading File 1" >> beam.io.ReadFromText('dept_data.txt')
                | 'Pair each employee with key' >> beam.Map(retTuple)          # {149633CM : [Marco,10,Accounts,1-01-2019]}
    
               )


loc_rows = ( 
                p1
                | "Reading File 2" >> beam.io.ReadFromText('location.txt') 
                | 'Pair each loc with key' >> beam.Map(retTuple)                # {149633CM : [9876843261,New York]}
               )


results = ({'dep_data': dep_rows, 'loc_data': loc_rows} 
           
           | beam.CoGroupByKey()
           | 'Write results' >> beam.io.WriteToText('data/result')
          )


p1.run()

!{('head -n 20 data/result-00000-of-00001')}