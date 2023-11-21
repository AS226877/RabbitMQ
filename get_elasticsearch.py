from elasticsearch import Elasticsearch

# Elasticsearch credentials
ES_USERNAME = 'elastic'
ES_PASSWORD = 'AK-kPmG0KtmLmVEWqV9Z'


# Function to get the Elasticsearch connection with authentication and SSL/TLS
def get_elasticsearch_connection():
    return Elasticsearch(
        ['https://localhost:9200'],
        basic_auth=(ES_USERNAME, ES_PASSWORD),
        ca_certs='http_ca.crt'
    )
