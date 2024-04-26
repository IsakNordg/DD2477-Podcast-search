import unittest

from backend.scraper.scraper import Scraper


class TestScraper(unittest.TestCase):

    scraper = Scraper(debug=False, debug_print=True)

    def test_scrape_set1(self):
        http_link_1 = 'https://anchor.fm/s/11b84b68/podcast/rss'
        episode_name_1 = '1: It’s Christmas Time!'
        url = self.scraper.scrape_audio_url(http_link_1, episode_name_1)
        self.assertEqual(url, "https://anchor.fm/s/11b84b68/podcast/play/9079164/"
                              "https%3A%2F%2Fd3ctxlq1ktw2nl.cloudfront.net%2Fproduction%2F"
                              "2019-11-18%2F39310279-44100-2-39e843297150c.m4a")

    def test_scrape_set2(self):
        http_link_2 = 'https://anchor.fm/s/b07181c/podcast/rss'
        episode_name_2 = 'The Goleta Postal Facility shootings- January 30 2020 - Today in True Crime History'
        url = self.scraper.scrape_audio_url(http_link_2, episode_name_2)
        self.assertEqual(url, "https://chrt.fm/track/4EB79A/pscrb.fm/rss/p/"
                              "traffic.megaphone.fm/GLSS1303936324.mp3?updated=1695653456")

    def test_scrape_set3(self):
        http_link_3 = 'https://anchor.fm/s/81a072c/podcast/rss'
        episode_name_3 = ('Ep.36 - Incorporating a Singular Goalkeeping Curriculum in the United States '
                          'w/ guest Phil Wheddon')
        url = self.scraper.scrape_audio_url(http_link_3, episode_name_3)
        self.assertEqual(url, "https://injector.simplecastaudio.com/e4ea7532-957a-495d-9674-821f581b23a3/"
                              "episodes/cb3b1941-db68-4a1f-a75e-0b6baf8a6f98/audio/128/default.mp3?"
                              "aid=rss_feed&awCollectionId=e4ea7532-957a-495d-9674-821f581b23a3&"
                              "awEpisodeId=cb3b1941-db68-4a1f-a75e-0b6baf8a6f98&feed=vv4BKCDj")

    def test_scrape_set4(self):
        http_link_4 = 'https://anchor.fm/s/917dba4/podcast/rss'
        episode_name_4 = 'Episode 1: Arrowhead Live! Debut'
        url = self.scraper.scrape_audio_url(http_link_4, episode_name_4)
        self.assertEqual(url, "https://traffic.megaphone.fm/APO9923946502.mp3")

    def test_scrape_set5(self):
        http_link_5 = 'https://www.fuckboisoflit.com/episodes?format=rss'
        episode_name_5 = 'The Lion, The Witch, And The Wardrobe - Ashley Beall'
        url = self.scraper.scrape_audio_url(http_link_5, episode_name_5)
        self.assertEqual(url, None)