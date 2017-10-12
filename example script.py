from mastodon import Mastodon

# Register app - only once!
'''
Mastodon.create_app(
     'pytooterapp',
     api_base_url = 'https://mastodon.social',
     to_file = 'pytooter_clientcred.secret'
)
'''

# Log in - either every time, or use persisted
'''
mastodon = Mastodon(
    client_id = 'pytooter_clientcred.secret',
    api_base_url = 'https://mastodon.social'
)
mastodon.log_in(
    'my_login_email@example.com',
    'incrediblygoodpassword',
    to_file = 'pytooter_usercred.secret'
)
'''

# Create actual API instance
mastodon = Mastodon(
    client_id = 'key.secret',
    access_token = 'access.secret',
    api_base_url = 'https://cybre.space'
)
mastodon.toot('Tooting from python using #mastodonpy !')
