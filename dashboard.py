from app import db
from booking import *
tc = Blueprint('trend_chart', __name__)

@tc.route('/trend_chart', methods=['GET'])
def trend_chartpage():
	if request.method == 'GET':
		output = dataOutput()
		
	return render_template('trend_chart.html', title='Package Chart', output = output)