def get_selector():

    selectors = {
        # Header
        "header_selector" : 'div.header',
        "header_left_container_selector" : 'div.left.header_side',

        # Logo
        "logo_container_selector" : 'div.logo_container',
        "logo_link_selector" : 'div.logo_container a',
        "logo_image_selector" : 'img.default_logo',

        # Navigation
        "menu_container_selector" : 'nav.main_menu_container',
        "menu_desktop_selector" : 'ul.menu.desktop-ul',
        "submenu_selector" : 'ul.sub-menu',
        "menu_list_item_selector" : 'li.menu-item',
        "menu_language_item_selector" : 'li.lang-item',
        "menu_mobile_selector" : 'ul.menu.mobile-ul',
        "menu_mobile_toggle_selector" : 'div.mobile-navigation-toggle',

        # Hero Image
        'hero_selector' : 'div.heroImage',
        'hero_image_container_selector' : 'div.header-img',
        'hero_image_selector' : 'div.header-img > img',
        'hero_title_container_selector' : 'div.page-category',
        'hero_title_text_selector' : 'div.page-category > h1#page-title',

        # Bio Profile
        "bio_profile_selector" : 'div.bio-profile',
        "bio_profile_image_container_selector" : 'div.bio-profile-image',
        "bio_profile_image_selector" : 'img.profile_image',
        'bio_profile_content_container_selector' : 'div.bio-profile-content',
        'bio_profile_text_container_selector' : 'div.profile-text',
        'bio_profile_title_selector' : 'div.profile-text > h2',
        'bio_profile_role_selector' : 'div.profile-text > h3',
        'bio_profile_role_link_selector' : 'div.profile-text > h3 a',
        'bio_profile_email_selector' : 'div.profile-text > h4',
        'bio_profile_email_link_selector' : 'div.profile-text > h4 a',
        'bio_profile_detail_selector' : 'div.bio-content',
        'bio_profile_detail_intro_selector' : 'div.bio-content p.content',
        'bio_profile_detail_showhide_selector' : 'div.bio-content a.show_hide',
        'bio_profile_detail_more_content_selector' : 'div.bio-content p.more_content',

        # YouTube Embed
        'youtube_embed_selector' : 'div.embed-youtube',
        'youtube_iframe_selector' : 'div.embed-youtube iframe',
        'youtube_bottom_section_selector' : 'div.cmp-youtube__footer',
        'youtube_accordion_selector' : 'div.cmp-youtube__footer div.accordion_1level',
        'youtube_accordion_header_selector' : 'div.cmp-youtube__footer div.accordion_1level div.main-title',
        'youtube_accordion_content_selector' : 'div.cmp-youtube__footer div.accordion_1level div.accordion_1_level_item',
        'youtube_download_container_selector' : 'div.cmp-youtube__download',
        'youtube_download_link_selector' : 'a.cmp-youtube__download-transcript',
        'youtube_download_link_text_selector' : 'span.cmp-youtube__download-transcript-text',
        'youtube_download_icon_selector' : 'span.cmp-youtube__download-transcript-icon',

        # Dummy
        'dummy_selector' : 'body',
    }

    return selectors
