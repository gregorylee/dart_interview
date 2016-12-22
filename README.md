#Sample code for Eric

- Created a Python script capable of handling 3rd party libraries and command line arguments to specify the elastic search host & source feed
    - Description: pulls down vulnerabilities from the exploit-db RSS feed and imports them into elastic
    - Application name: Vulminator
    - Github: https://github.com/gregorylee/dart_interview
- installing the application (with elastic running on 172.17.0.2)
    - git clone https://github.com/gregorylee/dart_interview.git
    - python setup.py install
    - vulminator  —es_host 172.17.0.2:9200