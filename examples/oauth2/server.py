# This example requires installing quart
from __future__ import annotations

from collections import Counter
import json

from quart import Quart, make_response, redirect, render_template, request
import stoat

app = Quart(__name__, template_folder='examples/oauth2/templates')


@app.get('/')
async def index():
    return await render_template('index.html')


@app.while_serving
async def lifespan():
    state = stoat.State()

    async with stoat.HTTPClient(state=state).attach() as http:
        app.config.from_object('examples.oauth2.config.Config')
        app.stoat_http = http  # type: ignore
        yield


@app.get('/oauth2/start')
async def start_oauth2_flow():
    return await render_template(
        'oauth2_start.html',
        client_id=json.dumps(app.config['CLIENT_ID']),
        redirect_uri=json.dumps(app.config['REDIRECT_URI']),
    )


@app.get('/oauth2/complete')
async def complete_oauth2_flow():
    http = app.stoat_http  # type: ignore
    assert isinstance(http, stoat.HTTPClient)

    if 'code' in request.args:
        code = request.args['code']
        client_id = app.config['CLIENT_ID']
        result = await http.exchange_token(
            code=code,
            client=client_id,
            client_secret=app.config['CLIENT_SECRET'],
            grant_type=stoat.OAuth2GrantType.authorization_code,
        )
        token = result.access_token
    else:
        token = request.cookies.get('token')
        if not token:
            return redirect('/oauth2/start')

    user = await http.get_me(http_overrides=stoat.HTTPOverrideOptions(bot=False, oauth2=True, token=token))

    relationship_status_to_count = Counter([r.status for r in user.relations.values()])
    payload = {
        'id': user.id,
        'name': user.name,
        'discriminator': user.discriminator,
        'blocked_count': relationship_status_to_count.get(stoat.RelationshipStatus.blocked, 0),
        'friend_count': relationship_status_to_count.get(stoat.RelationshipStatus.friend, 0),
        'incoming_friend_count': relationship_status_to_count.get(stoat.RelationshipStatus.incoming, 0),
        'outgoing_friend_count': relationship_status_to_count.get(stoat.RelationshipStatus.outgoing, 0),
    }

    response = await make_response(
        await render_template(
            'oauth2_complete.html',
            payload=json.dumps(payload),
        ),
    )
    response.set_cookie('token', token, max_age=604800)
    return response


app.run()
