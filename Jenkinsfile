node{
	git url:'https://github.com/yaduvanshilokesh/datapipeline_apache_beam.git'
	sh label: '', script: '''virtualenv .
    . ./bin/activate
    pip install apache-beam[gcp]
    python streaming.py --runner DataflowRunner --temp_location gs://mydatapipelinebucket/tmp --project testproject2-261014 --streaming &
    '''
}