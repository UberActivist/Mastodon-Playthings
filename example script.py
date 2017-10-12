from mastodon import Mastodon

mastodon = Mastodon(
    client_id = 'key.secret',
    access_token = 'access.secret',
    api_base_url = 'https://botsin.space'
)
mastodon.toot('Hello.')
