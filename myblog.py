# -*- coding:utf-8 -*-
import os
from app import app
from settings.prod_config import DEBUG

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=DEBUG)