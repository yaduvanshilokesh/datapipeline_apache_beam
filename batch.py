import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
class Parse:
        def method(self,line):
                keys = ['name','city','complain']
                val = line.split(",")
                return dict(zip(keys,val))
def run():
        options = PipelineOptions()
        p = beam.Pipeline(options=options)
        parse=Parse()
        lines = p | beam.io.ReadFromText("gs://mydatapipelinebucket/input.csv") | beam.Map(lambda s: parse.method(s)) | beam.io.WriteToBigQuery('testproject2-261014:mydataset.mydata',schema='name:string,city:string,complain:string',create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
        p.run().wait_until_finish()
if __name__ == '__main__':
  run()
