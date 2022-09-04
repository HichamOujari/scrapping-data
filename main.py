from elasticsearch import Elasticsearch

elastic_url = "localhost"
elastic_port = 9200

es = Elasticsearch(
    [{'host': elastic_url, 'port': elastic_port, "scheme": "https"}])

es.index(index='sentiment-index-news',
         doc_type="news-type",
         body={
             "Author": "author",
             "ID Berita": "id_berita",
         })
