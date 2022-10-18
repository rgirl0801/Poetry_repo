import pytest

from KateFox.pages.downloads_page import DownloadsPage


url = 'https://www.selenium.dev/downloads/'


@pytest.mark.main
class TestDownloadsPageClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.downloads_page = DownloadsPage(browser, url)
        self.downloads_page.open_page()

    def test_download_latest_verion(self, browser):
        self.downloads_page.download_latest_version()

    def test_possibility_to_see_documentation(self, browser):
        self.downloads_page.go_to_documentation_page()
        # TODO: add documentation page
