import sys
import argparse
import feedparser
from elasticsearch import Elasticsearch

def getScriptArgumentParser(args=sys.argv):
    """Return ArgumentParser object

    Kwargs:
        args (list):        list of arguments that will be parsed.  The default
                            is the sys.argv list, and should be correct for most
                            use cases.

    Returns:
        ArgumentParser object that can be used to validate and execute the
        current script invocation.
    """
    parser = argparse.ArgumentParser(
            description='ArgumentParser makes it easy to write user-friendly command-line interfaces using the argparse module. The program defines what arguments it requires, and ArgumentParser will figure out how to parse them')

    #parser.add_argument('--init',
    #        action='store_true',
    #        help="initialize elasticsearch doc type for atom feed. this option is exclusive & used during setup")
            
    parser.add_argument('--rss_url',
            default='https://www.exploit-db.com/rss.xml',
            help="Valid atom rss vulnerability feed url")
    
    parser.add_argument('--es_host',
            default='localhost',
            help="Valid connection host string for ElasticSearch server")
    
    return parser

"""
    Sample RSS Vuln Item (for schema reference)
    <title>[remote] - NETGEAR WNR2000v5 - Remote Code Execution</title>
    <link>https://www.exploit-db.com/exploits/40949/?rss</link>
    <description>NETGEAR WNR2000v5 - Remote Code Execution</description>
    <category>remote</category>
    <pubDate>Wed, 21 Dec 2016 00:00:00 +0000</pubDate>
    <guid isPermaLink="false">edb-40949</guid>
    """
class vulminator(object):
    def __init__(self, args):
        self.args=args
        self.es = Elasticsearch([args.es_host])

    def import_vulns(self):
        v = feedparser.parse(self.args.rss_url)
        for vuln in v.entries:
            del vuln['published_parsed']
            self.es.index(index='vuln-index', doc_type='atom_feed_item', id=vuln['id'], body=vuln)
        #self.es.indices.refresh(index='vuln-index')
        
        

def main():
    args = getScriptArgumentParser().parse_args()
    v = vulminator(args)
    #if v.args.init:
    #    VulnInfoItem.init() #add schema to ES
    v.import_vulns()

if __name__ == '__main__':
    main()