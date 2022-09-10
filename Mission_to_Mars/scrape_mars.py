# %%
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

    # %%
def scrape_mars():
    response = {}
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # %%
    url = "https://redplanetscience.com/"
    browser.visit(url)
    page = soup(browser.html)


    # %%

    response["news_titles"] = page.find("div", "content_title").text
    response["news_p"] = page.find("div", "article_teaser_body").text

    # %%
    url ="https://spaceimages-mars.com/"
    browser.visit(url)
    jpl_page = soup(browser.html)

    # %%
    response["featured_image_url"] = url + jpl_page.find("img", "headerimage")["src"]

    # %%
    url = "https://galaxyfacts-mars.com/"
    browser.visit(url)
    mars_fact_page = soup(browser.html)

    # %%
    mars_table = mars_fact_page.find("table").prettify()
    mars_df = pd.read_html(mars_table)[0]
    mars_df.columns = ["Description", "Mars", "Earth"]
    mars_df.set_index("Description", inplace=True)
    response["html_table"] = mars_df.to_html()

    # %%
    url = "https://marshemispheres.com/"
    browser.visit(url)
    mar_image_page = soup(browser.html)

    # %%
    mars_image_links = mar_image_page.find_all("div", "item")
    hemisphere_image_urls = []
    for link in mars_image_links:
        title = link.h3.text.rsplit(" ", 1)[0]
        browser.visit(url + link.a["href"])
        sphere_page = soup(browser.html)
        img_url = url + sphere_page.find("img", "wide-image")["src"]
        hemisphere_image_urls.append({"title":title, "img_url":img_url})
    response["hemisphere_image_urls"] = hemisphere_image_urls
    browser.quit()
    # %%
    return response

