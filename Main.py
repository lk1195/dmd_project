import DBLPCrawler
import BSCrawler
import Recorder
__author__ = 'lk1195'


# dblpCrawler = DBLPCrawler.DBLPCrawler()
# # dblpCrawler.get_books_by_link('http://dblp.uni-trier.de/db/journals/corr/corr1501.html')
# dblpCrawler.get_books_by_search("Cormen")


bsCrawler = BSCrawler.BSCrawler()
bsCrawler.get_books_by_search("Cormen")
