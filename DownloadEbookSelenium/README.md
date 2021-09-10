# Title

Test for downloading ebooks from https://www.salesmanago.com written in Python and Selenium library.

# Requirements

* `python 3.9`
* `selenium 3.141.0`
* `pytest 6.2.5`

# Installation

Using `virtualenv` install all required packages with:

```commandline
pip install -r requirements.txt
```

Script needs for working chromedriver.exe which can be downloaded from below location (be aware that main version 
of chromedriver must be the same as your Chrome browser version):
https://chromedriver.chromium.org/downloads

Additionally, it is required to place chromedriver executable file i.ex. at "C:\Test_Files" 
and add this location to windows PATH.

# Available EBOOK names (state for 10.09.2021)

* `data-ethics-preference-management`
* `cdp-vs-crm`
* `ai-product-recommendation-engines`
* `cookbok-of-marketing-automation-in-ecommerce`
* `definitive-guide-to-email-deliverability`
* `complete-guide-to-ma-in-ecommerce`
* `online_consumer_trends`
* `how_marketing_automation_is_transformed_by_ai_and_data_science`
* `ebook_live_chat`
* `10_success_stories_ebook`
* `product_profile_salesmanago_new_knowledge`
* `2018-european-digital-marketing-survey`
* `complete_gdpr_guidebook`
* `unique_selling_proposition`
* `12ideas_for_omnichannel_marketing`
* `ma_in_ecommerce_for_beginners`
* `socialmedia_ecommerce`
* `5_ecommerce_problems_2`
* `5_ecommerce_problems`
* `great_book_of_generating_leads_ebook`
* `ultimate_guide_to_push_notifications`
* `customer_value_marketing_new_knowledge`
* `pocket_dictionary_new_knowledge`
* `crisis_of_inbound_new_knowledge`
* `zmot_EN_new_knowledge`
* `switch_from_email_marketing`
* `Turn_visitors_new_knowledge`
* `mobile_marketing_new_knowledge`
* `amazing_shopping_experience_new_knowledge`
* `persona_new_knowledge`
* `iot_new_knowledge`
* `definitve_and_ultimate_new_knowledge`
* `Engagement_Marketing_new_knowledge`

# Run scenario using pytest

You need to invoke command window in location of project files and then write:
```commandline
pytest --stringinput name_of_ebook
```

# Run scenario without pytest

You need to invoke command window in location of project files and then write:
```commandline
python test_ebook_downloading.py ebook_name
```
