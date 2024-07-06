import typesense
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

client = typesense.Client({
    'nodes': [{
        'host': 'zjsxp3nl1oqih2vep-1.a1.typesense.net',  # For Typesense Cloud use xxx.a1.typesense.net
        'port': '443',       # For Typesense Cloud use 443
        'protocol': 'https'    # For Typesense Cloud use https
    }],
    'api_key': '2tOW7InWQ4wB18ZrG1c8a8NfT72G3Wx8',
    'connection_timeout_seconds': 2
})

def fetch_all_documents(collection_name, query_by):
    documents = []
    page = 1
    while True:
        response = client.collections[collection_name].documents.search({
            'q': '*',
            'query_by': query_by,  # Specify the fields to query by
            'per_page': 100,
            'page': page
        })
        documents.extend(response['hits'])
        logger.info(f'Fetched {len(response["hits"])} documents from {collection_name}, page {page}')
        if len(response['hits']) < 100:
            break
        page += 1
    return documents

def reindex_documents(documents, new_collection_name):
    for doc in documents:
        # Add default item_priority if not present
        if 'item_priority' not in doc['document']:
            doc['document']['item_priority'] = 0  # Default value
        # Add default url if not present
        if 'url' not in doc['document']:
            doc['document']['url'] = ""  # Default value
        client.collections[new_collection_name].documents.upsert(doc['document'])
        logger.info(f'Document with ID {doc["document"].get("id", "unknown")} reindexed to {new_collection_name}')

def verify_reindexing(new_collection_name):
    response = client.collections[new_collection_name].documents.search({
        'q': '*',
        'query_by': 'url',  # Use a common field
        'per_page': 10,
        'page': 1
    })
    logger.info(f'Total documents in {new_collection_name}: {response["found"]}')
    for hit in response['hits']:
        logger.info(f'Document ID: {hit["document"].get("id", "unknown")} - Content: {hit["document"]}')

# Fetch documents from each collection
logger.info('Fetching documents from collections...')
category_documents = fetch_all_documents('category', 'post_title')
page_documents = fetch_all_documents('page', 'post_title')
post_documents = fetch_all_documents('post', 'post_title')
# transpara_documents = fetch_all_documents('Transpara-Virtual-KPI_1717434908', 'content')
logger.info('Fetching complete.')

# Re-index documents into the new combined collection
logger.info('Reindexing documents...')
reindex_documents(category_documents, 'new_combined_collection')
reindex_documents(page_documents, 'new_combined_collection')
reindex_documents(post_documents, 'new_combined_collection')
# reindex_documents(transpara_documents, 'new_combined_collection')
logger.info('Reindexing complete.')

# Verify reindexing results
logger.info('Verifying reindexing results...')
verify_reindexing('new_combined_collection')
logger.info('Verification complete.')