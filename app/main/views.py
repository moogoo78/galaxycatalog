from app.main import main
from app.database import session
#from app.database import session
#from app.models import Dataset, Collection

@main.route('/foo')
def index():
    #ds = Dataset()
    #c = Collection()
    #c.name = 'non'
    #session.add(c)
    #session.commit()
    return ('foo')
