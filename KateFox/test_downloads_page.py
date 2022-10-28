import pytest

from KateFox.pages.downloads_page import DownloadsPage


@pytest.mark.main
class TestDownloadsPageClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.downloads_page = DownloadsPage(browser, url + 'downloads')


    def test_download_latest_verion(self):
        self.downloads_page.open_page()
        self.downloads_page.download_latest_version()

    def test_possibility_to_see_documentation(self, browser, url):
        self.downloads_page.open_page()
        self.downloads_page.go_to_documentation_page()
        self.downloads_page.page_is_open(url)
