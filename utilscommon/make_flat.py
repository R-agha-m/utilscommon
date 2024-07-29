SEPARATOR = "__"


def make_flat(
        data: dict | list | tuple | set,
        key: str = "",
        given_separator: str = SEPARATOR,
) -> dict:
    separator = given_separator if key else ""
    prepared_data = dict()
    if isinstance(data, dict):
        for key_i, value_i in data.items():
            prepared_data.update(make_flat(
                data=value_i,
                key=f'{key}{separator}{key_i}',
                given_separator=given_separator,
            ))

    elif isinstance(data, (list, tuple, set)):
        for index, value in enumerate(data):
            prepared_data.update(make_flat(
                data=value,
                key=f'{key}{separator}{index}',
                given_separator=given_separator,
            ))

    else:
        prepared_data[str(key)] = data

    return prepared_data

#
#
#
# a = {
#     "sections": [
#         {
#             "section_name": "IMAGE",
#             "widgets": [
#                 {
#                     "widget_type": "IMAGE_CAROUSEL",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.ImageCarouselData",
#                         "items": [
#                             {
#                                 "image_url": "",
#                                 "image": {
#                                     "url": "https://s100.divarcdn.com/static/photo/afra/post/Bshbjv0VhzTNs3fyUHjewg/742c58b7-c9bd-486a-9044-3acaa7b41c01.jpg",
#                                     "alt": "فروش کلنگی قیطریه ۴۱۵ متر بر ۱۴ با ۵۳۰ متر بنا|فروش زمین و کلنگی|تهران, قیطریه|دیوار",
#                                     "thumbnail_url": "https://s100.divarcdn.com/static/photo/afra/thumbnail/GgXmcNUSOlKnQ979aIq-Ng/742c58b7-c9bd-486a-9044-3acaa7b41c01.jpg"
#                                 },
#                                 "video_url": ""
#                             },
#                             {
#                                 "image_url": "",
#                                 "image": {
#                                     "url": "https://s100.divarcdn.com/static/photo/afra/post/Qb77zQgBPWCVAkHA03VTDA/c700a49e-9463-4ef3-bc00-1ae1251afe95.jpg",
#                                     "alt": "فروش کلنگی قیطریه ۴۱۵ متر بر ۱۴ با ۵۳۰ متر بنا|فروش زمین و کلنگی|تهران, قیطریه|دیوار",
#                                     "thumbnail_url": "https://s100.divarcdn.com/static/photo/afra/thumbnail/ckQRK81PC581ZwmvTi9heA/c700a49e-9463-4ef3-bc00-1ae1251afe95.jpg"
#                                 },
#                                 "video_url": ""
#                             },
#                             {
#                                 "image_url": "",
#                                 "image": {
#                                     "url": "https://s100.divarcdn.com/static/photo/afra/post/gUkdl2fENe8VS_azFFL0tQ/d39ce205-461a-4656-8bc9-a9a890dff1a6.jpg",
#                                     "alt": "فروش کلنگی قیطریه ۴۱۵ متر بر ۱۴ با ۵۳۰ متر بنا|فروش زمین و کلنگی|تهران, قیطریه|دیوار",
#                                     "thumbnail_url": "https://s100.divarcdn.com/static/photo/afra/thumbnail/Gyo_rgG7DrGwwqhVBm7qsQ/d39ce205-461a-4656-8bc9-a9a890dff1a6.jpg"
#                                 },
#                                 "video_url": ""
#                             }
#                         ],
#                         "padded": False,
#                         "image_aspect_ratio": {
#                             "dynamic_aspect_ratio": {
#                                 "height": 3,
#                                 "width": 4
#                             }
#                         },
#                         "has_preview": True,
#                         "has_thumbnails": True,
#                         "scale_type": "CENTER_CROP",
#                         "show_tooltip": False,
#                         "tooltip_data": None
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 }
#             ]
#         },
#         {
#             "section_name": "TITLE",
#             "widgets": [
#                 {
#                     "widget_type": "LEGEND_TITLE_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.LegendTitleRowData",
#                         "title": "فروش کلنگی قیطریه ۴۱۵ متر بر ۱۴ با ۵۳۰ متر بنا",
#                         "subtitle": "نیم ساعت پیش در تهران، قیطریه",
#                         "has_divider": True,
#                         "image_url": "https://s100.divarcdn.com/static/images/real-estate/3SJlh5qaXvSd9x1oP4Tg0Q.jpg",
#                         "tags": [],
#                         "show_thumbnail": True,
#                         "mobile_design": False,
#                         "high_level_heading": False
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 },
#                 {
#                     "widget_type": "SELECTOR_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.SelectorRowData",
#                         "title": "زنگ خطرهای قبل از معامله",
#                         "image_url": "",
#                         "action": {
#                             "type": "LOAD_PAGE",
#                             "payload": {
#                                 "@type": "type.googleapis.com/widgets.LoadPagePayload",
#                                 "title": "",
#                                 "widget_list": [
#                                     {
#                                         "widget_type": "BREADCRUMB",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.BreadcrumbData",
#                                             "parent_items": [
#                                                 {
#                                                     "title": "بازگشت به آگهی",
#                                                     "action": {
#                                                         "type": "HISTORY_BACK",
#                                                         "payload": None,
#                                                         "fallback_link": "",
#                                                         "page_pop_link": False
#                                                     }
#                                                 }
#                                             ],
#                                             "current_page_title": "",
#                                             "padded": True,
#                                             "item": None
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "PAGE_TITLE_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.PageTitleRowData",
#                                             "title": "روش‌های رایج کلاهبرداری در املاک",
#                                             "subtitle": ""
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "DESCRIPTION_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.DescriptionRowData",
#                                             "text": "- دریافت بیعانه\n- دریافت پول به بهانهٔ ارسال عکس و بازدید\n- اجاره یا فروش همزمان ملک به چند نفر\n- اجاره یا فروش ملک با سند یا شرایط مشکل‌دار\n",
#                                             "has_divider": False,
#                                             "is_primary": True,
#                                             "expandable": False,
#                                             "small": False,
#                                             "padded": True,
#                                             "preview_max_line": 0
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "PAGE_TITLE_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.PageTitleRowData",
#                                             "title": "در این موارد به شدت احتیاط کنید",
#                                             "subtitle": ""
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "FEATURE_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.FeatureRowData",
#                                             "title": "آگهی‌گذار درخواست بیعانه دارد",
#                                             "image_url": "",
#                                             "image_color": "UNKNOWN",
#                                             "has_divider": False,
#                                             "action": None,
#                                             "icon": {
#                                                 "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/error_primary/block.png",
#                                                 "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/error_primary/block.png",
#                                                 "icon_name": "BLOCK",
#                                                 "icon_color": "ERROR_PRIMARY"
#                                             },
#                                             "disabled": False,
#                                             "text_color": "UNKNOWN"
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "FEATURE_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.FeatureRowData",
#                                             "title": "قیمت ملک پایین و وسوسه‌کننده‌ است",
#                                             "image_url": "",
#                                             "image_color": "UNKNOWN",
#                                             "has_divider": False,
#                                             "action": None,
#                                             "icon": {
#                                                 "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/error_primary/block.png",
#                                                 "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/error_primary/block.png",
#                                                 "icon_name": "BLOCK",
#                                                 "icon_color": "ERROR_PRIMARY"
#                                             },
#                                             "disabled": False,
#                                             "text_color": "UNKNOWN"
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "FEATURE_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.FeatureRowData",
#                                             "title": "آگهی‌گذار به جای چت دیوار، مکالمه در خارج دیوار را پیشنهاد می‌کند",
#                                             "image_url": "",
#                                             "image_color": "UNKNOWN",
#                                             "has_divider": False,
#                                             "action": None,
#                                             "icon": {
#                                                 "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/error_primary/block.png",
#                                                 "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/error_primary/block.png",
#                                                 "icon_name": "BLOCK",
#                                                 "icon_color": "ERROR_PRIMARY"
#                                             },
#                                             "disabled": False,
#                                             "text_color": "UNKNOWN"
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "FEATURE_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.FeatureRowData",
#                                             "title": "وضعیت سند مشخص نیست",
#                                             "image_url": "",
#                                             "image_color": "UNKNOWN",
#                                             "has_divider": False,
#                                             "action": None,
#                                             "icon": {
#                                                 "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/error_primary/block.png",
#                                                 "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/error_primary/block.png",
#                                                 "icon_name": "BLOCK",
#                                                 "icon_color": "ERROR_PRIMARY"
#                                             },
#                                             "disabled": False,
#                                             "text_color": "UNKNOWN"
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "PAGE_TITLE_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.PageTitleRowData",
#                                             "title": "قبل از معامله بخوانید:",
#                                             "subtitle": ""
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "SELECTOR_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.SelectorRowData",
#                                             "title": "تصدیق اصالت اسناد و اوراق",
#                                             "image_url": "",
#                                             "action": {
#                                                 "type": "OPEN_WEB_PAGE",
#                                                 "payload": {
#                                                     "@type": "type.googleapis.com/widgets.OpenWebPagePayload",
#                                                     "link": "https://my.ssaa.ir/portal/estate/originality-document/",
#                                                     "page_type": "UNKNOWN",
#                                                     "nofollow": False
#                                                 },
#                                                 "fallback_link": "",
#                                                 "page_pop_link": False
#                                             },
#                                             "has_divider": True,
#                                             "has_notification": False,
#                                             "icon": {
#                                                 "image_url_dark": "",
#                                                 "image_url_light": "",
#                                                 "icon_name": "UNKNOWN",
#                                                 "icon_color": "UNKNOWN"
#                                             },
#                                             "notification_text": "",
#                                             "description": "",
#                                             "has_arrow": True,
#                                             "small": False,
#                                             "last_notification_date": "0001-01-01T00:00:00Z",
#                                             "uid": "",
#                                             "fullwidth": False
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "SELECTOR_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.SelectorRowData",
#                                             "title": "استعلام الکترونیکی ملک",
#                                             "image_url": "",
#                                             "action": {
#                                                 "type": "OPEN_WEB_PAGE",
#                                                 "payload": {
#                                                     "@type": "type.googleapis.com/widgets.OpenWebPagePayload",
#                                                     "link": "https://my.ssaa.ir/portal/ssar/request-status",
#                                                     "page_type": "UNKNOWN",
#                                                     "nofollow": False
#                                                 },
#                                                 "fallback_link": "",
#                                                 "page_pop_link": False
#                                             },
#                                             "has_divider": True,
#                                             "has_notification": False,
#                                             "icon": {
#                                                 "image_url_dark": "",
#                                                 "image_url_light": "",
#                                                 "icon_name": "UNKNOWN",
#                                                 "icon_color": "UNKNOWN"
#                                             },
#                                             "notification_text": "",
#                                             "description": "",
#                                             "has_arrow": True,
#                                             "small": False,
#                                             "last_notification_date": "0001-01-01T00:00:00Z",
#                                             "uid": "",
#                                             "fullwidth": False
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "SECTION_DIVIDER_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.SectionDividerRowData",
#                                             "padded": False
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "PAGE_TITLE_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.PageTitleRowData",
#                                             "title": "مشکلی برایتان پیش آمده است؟",
#                                             "subtitle": ""
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "DESCRIPTION_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.DescriptionRowData",
#                                             "text": "در صورت بروز مشکل و یا شناسایی نشانه‌های مشکوک، لطفاً آگهی را در صفحهٔ «گزارش کلاهبرداری و رفتار مشکوک» گزارش دهید.",
#                                             "has_divider": False,
#                                             "is_primary": True,
#                                             "expandable": False,
#                                             "small": False,
#                                             "padded": True,
#                                             "preview_max_line": 0
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "IMAGE_SLIDER_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.ImageSliderRowData",
#                                             "items": [
#                                                 {
#                                                     "image_url": "https://jobs.divarcdn.com/jobs-fraud-alert.png",
#                                                     "description": "",
#                                                     "video_url": "",
#                                                     "action_log": None
#                                                 }
#                                             ],
#                                             "show_tooltip": False,
#                                             "tooltip_data": None,
#                                             "scale_type": "CENTER_CROP",
#                                             "background_color": "TRANSPARENT"
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     },
#                                     {
#                                         "widget_type": "SUBTITLE_ROW",
#                                         "data": {
#                                             "@type": "type.googleapis.com/widgets.SubtitleRowData",
#                                             "text": "آخرین بروزرسانی: شهریور ۱۴۰۲",
#                                             "has_divider": False,
#                                             "disabled": False,
#                                             "small": False,
#                                             "type": "UNKNOWN"
#                                         },
#                                         "action_log": None,
#                                         "cache": None,
#                                         "visibility_condition": [],
#                                         "uid": ""
#                                     }
#                                 ],
#                                 "sticky_widget": None,
#                                 "slug": "",
#                                 "action_log": None,
#                                 "show_bottom_bar": False,
#                                 "presentation": None
#                             },
#                             "fallback_link": "",
#                             "page_pop_link": False
#                         },
#                         "has_divider": True,
#                         "has_notification": False,
#                         "icon": {
#                             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/warning.png",
#                             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/warning.png",
#                             "icon_name": "WARNING",
#                             "icon_color": "ICON_SECONDARY"
#                         },
#                         "notification_text": "",
#                         "description": "",
#                         "has_arrow": True,
#                         "small": False,
#                         "last_notification_date": "0001-01-01T00:00:00Z",
#                         "uid": "",
#                         "fullwidth": False
#                     },
#                     "action_log": {
#                         "server_side_info": {
#                             "item_type": {
#                                 "type": "POST_WARNING"
#                             },
#                             "info": {
#                                 "@type": "type.googleapis.com/action_log.PostWarningInfo",
#                                 "post_token": "gZYevtD1"
#                             }
#                         },
#                         "enabled": True
#                     },
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 }
#             ]
#         },
#         {
#             "section_name": "NOTE",
#             "widgets": [
#                 {
#                     "widget_type": "NOTE",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.NoteData",
#                         "title": "یادداشت من",
#                         "button_title": "ویرایش یادداشت",
#                         "post_token": "gZYevtD1"
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 }
#             ]
#         },
#         {
#             "section_name": "DESCRIPTION",
#             "widgets": [
#                 {
#                     "widget_type": "SECTION_TITLE_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.SectionTitleRowData",
#                         "title": "توضیحات",
#                         "subtitle": "",
#                         "image_url": "",
#                         "padded": False,
#                         "action": None,
#                         "action_title": "",
#                         "title_color": "TEXT_PRIMARY",
#                         "padding": "UNKNOWN"
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 },
#                 {
#                     "widget_type": "DESCRIPTION_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.DescriptionRowData",
#                         "text": "✅ منطقه : قیطریه \n✅ مساحت زمین : ۴۱۵ متر مربع\n▪️بر ملک : ۱۴ متر \n▪️بنای مفید موجود: ۵۳۰ مترمربع \n▪️تعدا طبقات : ۳ طبقه \n▪️گذر کوچه : ۱۲ متر\n▪️پهنه ملک :مسکونی \n\n▪️مناسب ساخت ، سکونت\n▪️فایل جهت فروش یا مشارکت ویا معاوضه \n\n✅ ارائه خدمات خرید و فروش ملکی شامل :\n▪️خرید و فروش ویلا در لواسان و ...\n▪️پنت هاوس\n▪️ویلایی،مستغلات،کلنگی و مشارکت،زمین، اداری و تجاری\n▪️پیش فروش\n▪️معاوضه\n\n✅فایلینگ جامع در مناطق :\nخیابان ولیعصر،خیابان شریعتی\nفرمانیه،نیاوران،اقدسیه،گلستان شمالی، آجودانیه،الهیه و فرشته،زعفرانیه، ولنجک،محمودیه،قیطریه،پاسدران،دروس، دولت،جردن،ونک و ...\n\n✅خدمت رسانی حتی در ایام تعطیل\n✅پاسخ گویی ۲۴ ساعته و مشاوره رایگان\n\n✅ارائه خدمات وانجام کارشناسی و اعلام قیمت کارشناسی ملک بصورت رایگان دراسرع وقت \n\nخانم یکتا",
#                         "has_divider": False,
#                         "is_primary": True,
#                         "expandable": False,
#                         "small": False,
#                         "padded": False,
#                         "preview_max_line": 0
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 }
#             ]
#         },
#         {
#             "section_name": "STATIC",
#             "widgets": [
#                 {
#                     "widget_type": "BOOLEAN_RATE_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.BooleanRateRowData",
#                         "text": "بازخورد شما دربارهٔ این آگهی چیست؟",
#                         "submission_request_path": "post-quality/feedback",
#                         "submission_payload": {
#                             "category_hierarchy": [
#                                 "plot-old",
#                                 "residential-sell",
#                                 "real-estate",
#                                 "root"
#                             ],
#                             "post_token": "gZYevtD1",
#                             "type": "post"
#                         },
#                         "default_rate": "EMPTY"
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 },
#                 {
#                     "widget_type": "SELECTOR_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.SelectorRowData",
#                         "title": "گزارش کلاهبرداری و رفتار مشکوک",
#                         "image_url": "",
#                         "action": {
#                             "type": "OPEN_SCHEMA_PAGE",
#                             "payload": {
#                                 "@type": "type.googleapis.com/widgets.OpenSchemaPagePayload",
#                                 "request_path": "/report-reasons/openschema-v2/POST_DETAIL/plot-old/gZYevtD1",
#                                 "additional_data": {
#                                     "@type": "type.googleapis.com/customer_trust.GetOpenSchemaReportReasonsRequest.AdditionalData",
#                                     "token": "gZYevtD1",
#                                     "category": "plot-old",
#                                     "source": "POST_DETAIL"
#                                 },
#                                 "page": "UNKNOWN_PAGE",
#                                 "is_modal": True,
#                                 "rest_request_path": "/report-reasons/openschema-v2/POST_DETAIL/plot-old/gZYevtD1",
#                                 "grpc_request_path": "/customer_trust.Reports/GetOpenSchemaReportReasonsV2"
#                             },
#                             "fallback_link": "",
#                             "page_pop_link": False
#                         },
#                         "has_divider": True,
#                         "has_notification": False,
#                         "icon": {
#                             "image_url_dark": "https://s100.divarcdn.com/static/imgs/widget-icons/dark/icon_secondary/report.png",
#                             "image_url_light": "https://s100.divarcdn.com/static/imgs/widget-icons/light/icon_secondary/report.png",
#                             "icon_name": "REPORT",
#                             "icon_color": "ICON_SECONDARY"
#                         },
#                         "notification_text": "",
#                         "description": "",
#                         "has_arrow": True,
#                         "small": True,
#                         "last_notification_date": "0001-01-01T00:00:00Z",
#                         "uid": "",
#                         "fullwidth": False
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 }
#             ]
#         },
#         {
#             "section_name": "TAGS",
#             "widgets": [
#                 {
#                     "widget_type": "WRAPPER_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.WrapperRowData",
#                         "chip_list": {
#                             "chips": [
#                                 {
#                                     "text": "فروش زمین و کلنگی",
#                                     "icon": None,
#                                     "type": "ACTION",
#                                     "style": "NORMAL",
#                                     "rounded": False,
#                                     "small": False,
#                                     "action": {
#                                         "type": "OPEN_POSTLIST_PAGE",
#                                         "payload": {
#                                             "@type": "type.googleapis.com/widgets.OpenPostListPagePayload",
#                                             "jli": None,
#                                             "web_url": "tehran/buy-old-house",
#                                             "no_cat_page": False,
#                                             "source_view": "UNKNOWN",
#                                             "tooltip": "",
#                                             "change_city": None
#                                         },
#                                         "fallback_link": "",
#                                         "page_pop_link": False
#                                     }
#                                 },
#                                 {
#                                     "text": "فروش زمین و کلنگی در قیطریه",
#                                     "icon": None,
#                                     "type": "ACTION",
#                                     "style": "NORMAL",
#                                     "rounded": False,
#                                     "small": False,
#                                     "action": {
#                                         "type": "OPEN_POSTLIST_PAGE",
#                                         "payload": {
#                                             "@type": "type.googleapis.com/widgets.OpenPostListPagePayload",
#                                             "jli": None,
#                                             "web_url": "tehran/buy-old-house/qeytarieh",
#                                             "no_cat_page": False,
#                                             "source_view": "UNKNOWN",
#                                             "tooltip": "",
#                                             "change_city": None
#                                         },
#                                         "fallback_link": "",
#                                         "page_pop_link": False
#                                     }
#                                 }
#                             ]
#                         },
#                         "padded": False
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 }
#             ]
#         },
#         {
#             "section_name": "BUSINESS_SECTION",
#             "widgets": [
#                 {
#                     "widget_type": "EVENT_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.EventRowData",
#                         "title": "مسکن آکس",
#                         "subtitle": "همهٔ آگهی‌ها و اطلاعات آژانس",
#                         "has_indicator": False,
#                         "image_url": "https://s100.divarcdn.com/static/images/real-estate/3SJlh5qaXvSd9x1oP4Tg0Q.jpg",
#                         "label": "",
#                         "has_divider": False,
#                         "action": {
#                             "type": "REAL_ESTATE_AGENCY_PAGE",
#                             "payload": {
#                                 "@type": "type.googleapis.com/widgets.RealEstateAgencyPagePayload",
#                                 "business_ref": "239",
#                                 "slug": "ej6ms0eC"
#                             },
#                             "fallback_link": "",
#                             "page_pop_link": False
#                         },
#                         "type": "NORMAL",
#                         "padded": False,
#                         "hide_image": False,
#                         "counter": 0,
#                         "icon": None,
#                         "label_v_align": "TOP",
#                         "has_score": False,
#                         "percentage_score": 0,
#                         "score_subtitle": "",
#                         "score_color": "UNKNOWN",
#                         "last_notification_time": "0001-01-01T00:00:00Z",
#                         "uid": ""
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 }
#             ]
#         },
#         {
#             "section_name": "BREADCRUMB",
#             "widgets": [
#                 {
#                     "widget_type": "BREADCRUMB",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.BreadcrumbData",
#                         "parent_items": [
#                             {
#                                 "title": "املاک",
#                                 "action": {
#                                     "type": "OPEN_POSTLIST_PAGE",
#                                     "payload": {
#                                         "@type": "type.googleapis.com/widgets.OpenPostListPagePayload",
#                                         "jli": None,
#                                         "web_url": "tehran/real-estate",
#                                         "no_cat_page": False,
#                                         "source_view": "UNKNOWN",
#                                         "tooltip": "",
#                                         "change_city": None
#                                     },
#                                     "fallback_link": "",
#                                     "page_pop_link": False
#                                 }
#                             },
#                             {
#                                 "title": "فروش مسکونی",
#                                 "action": {
#                                     "type": "OPEN_POSTLIST_PAGE",
#                                     "payload": {
#                                         "@type": "type.googleapis.com/widgets.OpenPostListPagePayload",
#                                         "jli": None,
#                                         "web_url": "tehran/buy-residential",
#                                         "no_cat_page": False,
#                                         "source_view": "UNKNOWN",
#                                         "tooltip": "",
#                                         "change_city": None
#                                     },
#                                     "fallback_link": "",
#                                     "page_pop_link": False
#                                 }
#                             },
#                             {
#                                 "title": "فروش زمین و کلنگی",
#                                 "action": {
#                                     "type": "OPEN_POSTLIST_PAGE",
#                                     "payload": {
#                                         "@type": "type.googleapis.com/widgets.OpenPostListPagePayload",
#                                         "jli": None,
#                                         "web_url": "tehran/buy-old-house",
#                                         "no_cat_page": False,
#                                         "source_view": "UNKNOWN",
#                                         "tooltip": "",
#                                         "change_city": None
#                                     },
#                                     "fallback_link": "",
#                                     "page_pop_link": False
#                                 }
#                             }
#                         ],
#                         "current_page_title": "فروش کلنگی قیطریه ۴۱۵ متر بر ۱۴ با ۵۳۰ متر بنا",
#                         "padded": True,
#                         "item": None
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 }
#             ]
#         },
#         {
#             "section_name": "SUGGESTION",
#             "widgets": []
#         },
#         {
#             "section_name": "LIST_DATA",
#             "widgets": [
#                 {
#                     "widget_type": "UNEXPANDABLE_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.UnexpandableRowData",
#                         "title": "متراژ",
#                         "value": "۴۱۵ متر",
#                         "action": None,
#                         "has_divider": True,
#                         "compact": False,
#                         "has_copy_to_clipboard": False
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 },
#                 {
#                     "widget_type": "UNEXPANDABLE_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.UnexpandableRowData",
#                         "title": "قیمت کل",
#                         "value": "۱۴۷٬۰۰۰٬۰۰۰٬۰۰۰ تومان",
#                         "action": None,
#                         "has_divider": True,
#                         "compact": False,
#                         "has_copy_to_clipboard": False
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 },
#                 {
#                     "widget_type": "UNEXPANDABLE_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.UnexpandableRowData",
#                         "title": "قیمت هر متر",
#                         "value": "۳۵۴٬۲۱۶٬۰۰۰ تومان",
#                         "action": None,
#                         "has_divider": True,
#                         "compact": False,
#                         "has_copy_to_clipboard": False
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 },
#                 {
#                     "widget_type": "UNEXPANDABLE_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.UnexpandableRowData",
#                         "title": "آژانس املاک",
#                         "value": "مسکن آکس",
#                         "action": {
#                             "type": "REAL_ESTATE_AGENCY_PAGE",
#                             "payload": {
#                                 "@type": "type.googleapis.com/widgets.RealEstateAgencyPagePayload",
#                                 "business_ref": "239",
#                                 "slug": "ej6ms0eC"
#                             },
#                             "fallback_link": "",
#                             "page_pop_link": False
#                         },
#                         "has_divider": True,
#                         "compact": False,
#                         "has_copy_to_clipboard": False
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 },
#                 {
#                     "widget_type": "UNEXPANDABLE_ROW",
#                     "data": {
#                         "@type": "type.googleapis.com/widgets.UnexpandableRowData",
#                         "title": "مشاور املاک",
#                         "value": "خانم یکتا",
#                         "action": {
#                             "type": "REAL_ESTATE_AGENCY_PAGE",
#                             "payload": {
#                                 "@type": "type.googleapis.com/widgets.RealEstateAgencyPagePayload",
#                                 "business_ref": "",
#                                 "slug": "agent_qvqDMmNA"
#                             },
#                             "fallback_link": "",
#                             "page_pop_link": False
#                         },
#                         "has_divider": True,
#                         "compact": False,
#                         "has_copy_to_clipboard": False
#                     },
#                     "action_log": None,
#                     "cache": None,
#                     "visibility_condition": [],
#                     "uid": ""
#                 }
#             ]
#         }
#     ],
#     "share": {
#         "title": "فروش کلنگی قیطریه ۴۱۵ متر بر ۱۴ با ۵۳۰ متر بنا",
#         "web_url": "https://divar.ir/v/gZYevtD1",
#         "image_url": "https://s100.divarcdn.com/static/thumbnails/1721300929/gZYevtD1.jpg"
#     },
#     "seo": {
#         "title": "فروش کلنگی قیطریه ۴۱۵ متر بر ۱۴ با ۵۳۰ متر بنا|فروش زمین و کلنگی|تهران، قیطریه|دیوار",
#         "description": "فروش کلنگی قیطریه ۴۱۵ متر بر ۱۴ با ۵۳۰ متر بنا|فروش زمین و کلنگی|تهران، قیطریه|خرید و فروش ✅ منطقه : قیطریه \n✅ مساحت زمین : ۴۱۵ متر مربع\n▪️بر ملک : ۱۴ متر \n▪️بنای مفید موجود: ۵۳۰ مترمربع \n▪️تعدا طبقات : ۳ طبقه \n▪️گذر کوچه : ۱۲ متر\n▪️پهنه ملک :مسکونی \n\n▪️مناسب ساخت ، سکونت\n▪️فایل جهت فروش یا مشارکت ویا معاوضه \n\n✅ ارائه خدمات خرید و فروش ملکی شامل :\n▪️خرید و فروش ویلا در لواسان و ...\n▪️پنت هاوس\n▪️ویلایی،مستغلات،کلنگی و مشارکت،زمین، اداری و تجاری\n▪️پیش فروش\n▪️معاوضه\n\n✅فایلینگ جامع در مناطق :\nخیابان ولیعصر،خیابان شریعتی\nفرمانیه،نیاوران،اقدسیه،گلستان شمالی، آجودانیه،الهیه و فرشته،زعفرانیه، ولنجک،محمودیه،قیطریه،پاسدران،دروس، دولت،جردن،ونک و ...\n\n✅خدمت رسانی حتی در ایام تعطیل\n✅پاسخ گویی ۲۴ ساعته و مشاوره رایگان\n\n✅ارائه خدمات وانجام کارشناسی و اعلام قیمت کارشناسی ملک بصورت رایگان دراسرع وقت \n\nخانم یکتا| سایت ثبت آگهی، نیازمندی و خرید و فروش دیوار",
#         "android_package_name": "ir.divar",
#         "android_app_url": "android-app://ir.divar/http/v/فروش کلنگی قیطریه ۴۱۵ متر بر ۱۴ با ۵۳۰ متر بنا/gZYevtD1/",
#         "web_info": {
#             "title": "فروش کلنگی قیطریه ۴۱۵ متر بر ۱۴ با ۵۳۰ متر بنا",
#             "district_persian": "قیطریه",
#             "city_persian": "تهران",
#             "category_slug_persian": "فروش زمین و کلنگی"
#         },
#         "unavailable_after": "2024-08-18T14:38:49.673358"
#     },
#     "contact": {
#         "chat_enabled": False,
#         "apply_enabled": False,
#         "suspicion_alert": None,
#         "transaction": {
#             "enabled": False,
#             "confirmation_required": False,
#             "confirmation_text": ""
#         }
#     },
#     "webengage": {
#         "brand_model": "",
#         "business_ref": "239",
#         "business_type": "real-estate-business",
#         "cat_1": "real-estate",
#         "cat_2": "residential-sell",
#         "cat_3": "plot-old",
#         "category": "plot-old",
#         "city": "tehran",
#         "credit": 0,
#         "district": "qeytariyeh",
#         "gender": "",
#         "image_count": 3,
#         "originality": "",
#         "price": {
#             "$numberLong": "147000000512"
#         },
#         "rent": 0,
#         "status": "",
#         "token": "gZYevtD1"
#     },
#     "analytics": {
#         "cat1": "real-estate",
#         "cat2": "residential-sell",
#         "cat3": "plot-old",
#         "city": "tehran"
#     }
# }
