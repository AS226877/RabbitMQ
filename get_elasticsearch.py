from elasticsearch import Elasticsearch

# Elasticsearch credentials
es_username = 'elastic'
es_password = 'AK-kPmG0KtmLmVEWqV9Z'


# Function to get the Elasticsearch connection with authentication and SSL/TLS
def get_elasticsearch_connection():
    return Elasticsearch(
        ['https://localhost:9200'],
        basic_auth=(es_username, es_password),
        ca_certs='http_ca.crt'
    )
