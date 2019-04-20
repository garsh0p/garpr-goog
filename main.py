# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging
import os
import urlparse
import challonge

# [START imports]
import flask
# [END imports]

# [START create_app]
app = flask.Flask(__name__)
# [END create_app]


@app.route('/')
def home():
    return flask.render_template('index.html')


@app.route('/upload_tournament', methods=['POST'])
def upload_tournament():
    url = flask.request.form['url']
    parsed_url = urlparse.urlparse(url)
    split_netloc = parsed_url.netloc.split('.')
    if len(split_netloc) == 3 and split_netloc[0] != 'www':
        subdomain = split_netloc[0]
    else:
        subdomain = ''
    path = parsed_url.path.strip('/')

    if subdomain:
        challonge_id = subdomain + '-' + path
    else:
        challonge_id = path

    scraper = challonge.ChallongeScraper(challonge_id)

    print scraper.get_players()
    print scraper.get_matches()

    return flask.jsonify({
        'players': scraper.get_players(),
        'matches': scraper.get_matches()
    })


# [START form]
@app.route('/form')
def form():
    return flask.render_template('form.html')
# [END form]


# [START submitted]
@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = flask.request.form['name']
    email = flask.request.form['email']
    site = flask.request.form['site_url']
    comments = flask.request.form['comments']

    # [END submitted]
    # [START render_template]
    return flask.render_template(
        'submitted_form.html',
        name=name,
        email=email,
        site=site,
        comments=comments)
    # [END render_template]


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
