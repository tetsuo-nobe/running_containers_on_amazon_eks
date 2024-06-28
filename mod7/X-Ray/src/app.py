from flask import Flask, render_template
import json
import boto3
import datetime
import os
import logging
#
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
#
from aws_xray_sdk.core import patch
#
from botocore.config import Config
from botocore.exceptions import NoCredentialsError,ClientError
patch(['boto3'])

app = Flask(__name__)
app.logger.setLevel(logging.INFO)
#
xray_recorder.configure(service='python-web-xray')
XRayMiddleware(app, xray_recorder)
#
region = os.environ['REGION']
qname = os.environ['QUEUE_NAME']


@app.route('/')
def index():
    #
    return render_template('index.html')

@app.route('/<name>')
def hello(name):
    #
    return render_template('hello.html', title='Hello Page', name=name)
    
@app.route('/sqs/<message>')
def sendMessage(message):
    # キューの名前を指定してインスタンスを取得
    try:
      sqs = boto3.resource('sqs', region_name=region)
      queue = sqs.get_queue_by_name(QueueName=qname)
      queue.send_message(MessageBody=message)
    except NoCredentialsError as nocrederr:
      app.logger.error("!!!! InvalidCredentials !!!!")
      app.logger.error(nocrederr)
    except ClientError as clienterr:
      app.logger.error('!!!! ClientError !!!!')
      app.logger.error(clienterr)
      error_code = clienterr.response['Error']['Code']
      app.logger.error('error_code=%s',error_code)
    except Exception as ex:
      app.logger.error('!!!! Exception !!!!')
      app.logger.error(ex)
    #
    return render_template('result.html', title='Result Page', message=message)

if __name__ == "__main__":
  app.logger.info('---- start __main__ ----')
  app.logger.info(region)
  app.logger.info(qname)
  app.run(debug=True, host='0.0.0.0', port=8000)