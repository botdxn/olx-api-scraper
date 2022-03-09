from olx-api-scraper.scrape import make_url, get_list_of_ads


def test_scrape():
    assert isinstance(make_url("legnica", 500, 1000), str)
    assert isinstance(get_list_of_ads(make_url("legnica", 500, 1000), list):wq

    pass
