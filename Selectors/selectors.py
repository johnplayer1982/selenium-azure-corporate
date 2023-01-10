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
        "menu_desktop_top_level_with_submenu" : 'ul.menu.desktop-ul > li.menu-item.menu-item-has-children',
        "submenu_selector" : 'ul.sub-menu',
        "menu_list_item_selector" : 'li.menu-item',
        "menu_list_item_link_selector" : "li.menu-item > a",
        "menu_language_item_selector" : 'li.lang-item',
        # Mobile specific
        "menu_mobile_toggle_selector" : 'div.mobile-navigation-toggle',
        "menu_mobile_selector" : 'ul.menu.mobile-ul',
        "menu_mobile_items_selector" : 'ul.menu.mobile-ul > li.menu-item-has-children',
        'menu_mobile_item_link_selector' : '> a',
        "menu_mobile_sub_items_selector" : 'ul.menu.mobile-ul > li.menu-item-has-children ul.sub-menu',

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
        'youtube_accordion_header_selector' : 'div.accordion_1level div.main-title',
        'youtube_accordion_content_selector' : 'div.accordion_1level div.accordion_1_level_item',
        'youtube_accordion_content_text_selector' : 'div.accordion_1level div.accordion_1_level_item > p',

        'youtube_download_container_selector' : 'div.cmp-youtube__download',
        'youtube_download_link_selector' : 'a.cmp-youtube__download-transcript',
        'youtube_download_link_text_selector' : 'span.cmp-youtube__download-transcript-text',
        'youtube_download_icon_selector' : 'span.cmp-youtube__download-transcript-icon',

        # Accordion
        'accordion_selector' : 'div.accordion',
        'accordion_main_title_selector' : 'div.main-title',
        'accordion_sub_item' : 'div.item',
        'accordion_sub_item_content' : 'div.cmp-mps-accordion__sub-text',

        # Image
        'image_container_selector' : 'div.image',
        'image_innaer_container_selector' : 'div.cmp-image',
        'image_no_link_selector' : 'div.cmp-image__no-link',
        'image_with_link_selector' : 'a.cmp-image__link',

        # Buttons
        'button_container_selector' : 'div.button',
        'button_inner_container_selector' : 'div.cmp-button',
        'primary_button_selector' : 'a.cmp-button__primary',
        'secondary_button_selector' : 'a.cmp-button__secondary',

        # Dummy
        'dummy_selector' : 'body',
    }

    return selectors
