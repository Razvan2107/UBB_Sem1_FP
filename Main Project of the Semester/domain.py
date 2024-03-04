from validators import CarteValidator,ClientValidator,Inchiriere_ReturnareValidator
from console import Console
from repo_books import InMemoryRepositoryBooks,BookFileRepo,test_all_books_repo
from repo_customers import InMemoryRepositoryCustomers,CustomerFileRepo,test_all_customers_repo
from repo_hires_returns import InMemoryRepositoryHires_Returns,Hires_ReturnsFileRepo
from service import CarteService,ClientService,Inchirieri_ReturnariService,test_all_books_service,test_all_customers_service

repo1=BookFileRepo('books.txt','raport.txt')
val1=CarteValidator()
srv_books=CarteService(repo1,val1)

#repo1=InMemoryRepositoryBooks()
#val1=CarteValidator()
#srv_books=CarteService(repo1,val1)

#test_all_books_repo()
#test_all_books_service()

repo2=CustomerFileRepo('customers.txt')
val2=ClientValidator()
srv_customers=ClientService(repo2,val2)

# repo2=InMemoryRepositoryCustomers()
# val2=ClientValidator()
# srv_customers=ClientService(repo2,val2)

#test_all_customers_repo()
#test_all_customers_service()

#ui=Console(srv_books,srv_customers)
#ui.ui()

repo3=Hires_ReturnsFileRepo('hires.txt','returns.txt')
val3=Inchiriere_ReturnareValidator()
srv_hires_returns=Inchirieri_ReturnariService(repo3,val3)

#repo3=InMemoryRepositoryHires_Returns()
#val3=Inchiriere_ReturnareValidator()
#srv_hires_returns=Inchirieri_ReturnariService(repo3,val3)

ui=Console(srv_books,srv_customers,srv_hires_returns)
ui.ui()







